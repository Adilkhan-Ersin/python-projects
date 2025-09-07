document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  // Submit a message
  document.querySelector('#compose-form').addEventListener('submit', send_email);

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';
  document.querySelector('#emails-detail-view').style.display = 'none';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
}

function load_mailbox(mailbox) {

  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#emails-detail-view').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  // Get the emails
  fetch(`/emails/${mailbox}`)
  .then(response => response.json())
  .then(emails => {
      // Loop through emails
      console.log(emails);
      emails.forEach(singleEmail => {
        // Craete a div
        const newEmail = document.createElement('div');
        newEmail.style = `${singleEmail.read ? 'background-color: #cccccc' : 'background-color: #ffffff'}`
        newEmail.className = 'list-group-item d-flex align-items-center justify-content-between p-3 border';
        newEmail.innerHTML = `
          <div>
            <h5 class="mb-1">${singleEmail.sender}</h5>
            <h6 class="mb-1 text-muted">${singleEmail.subject}</h6>
          </div>
          <p class="mb-0 text-secondary">${singleEmail.timestamp}</p>
        `;
        // add click listener
        newEmail.addEventListener('click', () => view_email(singleEmail.id));
        document.querySelector('#emails-view').append(newEmail);
      })
  });
}

function send_email() {
  event.preventDefault();
  // Store fields
  const recipients = document.querySelector('#compose-recipients').value;
  const subject = document.querySelector('#compose-subject').value;
  const body = document.querySelector('#compose-body').value;

  // Send data
  fetch('/emails', {
    method: 'POST',
    body: JSON.stringify({
        recipients: recipients,
        subject: subject,
        body: body
    })
  })
  .then(response => response.json())
  .then(result => {
      // Print result
      console.log(result);
      load_mailbox('sent');
  });
}

function view_email(id) {
  fetch(`/emails/${id}`)
  .then(response => response.json())
  .then(email => {
      // Print email
      console.log(email);

      document.querySelector('#emails-view').style.display = 'none';
      document.querySelector('#compose-view').style.display = 'none';
      document.querySelector('#emails-detail-view').style.display = 'block';

      document.querySelector('#emails-detail-view').className = '';

      document.querySelector('#emails-detail-view').innerHTML = `
        <div class="d-flex align-items-center justify-content-between">
          <h3 class="w-100">${email.subject}</h3>
          <div class="d-flex align-items-center">
            <button class="mx-1 btn btn-sm btn-outline-info" id="reply">Reply</button>
            <button class="mx-1 btn btn-sm ${email.archived ? 'btn-outline-success' : 'btn-outline-warning'}" id="archive">${email.archived ? 'Unarchive' : 'Archive'}</button>
            <button class="mx-1 btn btn-sm btn-outline-danger" id="delete">Delete</button>
          </div>
        </div>
        <div class="d-flex align-items-center justify-content-between mb-3">
          <div class="d-block">
            <h4 class="mb-1">From: ${email.sender}</h4>
            <h5 class="mb-1 text-muted">To: ${email.recipients}</h5>
          </div>
          <p>Timestamp: ${email.timestamp}</p>
        </div>
        <div style="height: 60vh">
          <h4>Message:</h4>
          <p class="h6 h-50 border p-2">${email.body}</p>
        </div>
      `;

      // change read status
      if(!email.read) {
        fetch(`/emails/${id}`, {
          method: 'PUT',
          body: JSON.stringify({
            read: true
          })
        })
      }

      document.querySelector('#archive').addEventListener('click', () => archive_email(email.id, email.archived));
      document.querySelector('#reply').addEventListener('click', () => reply_email(email.id));
      document.querySelector('#delete').addEventListener('click', () => delete_email(email.id));

  });
}

function archive_email(id, isArchived) {
  fetch(`/emails/${id}`, {
    method: 'PUT',
    body: JSON.stringify({
        archived: !isArchived
    })
  })
  .then(() => load_mailbox('inbox'));
}

function reply_email(id) {
  fetch(`/emails/${id}`)
  .then(response => response.json())
  .then(email => {
      // Print email
      console.log(email);
      document.querySelector('#emails-view').style.display = 'none';
      document.querySelector('#compose-view').style.display = 'block';
      document.querySelector('#emails-detail-view').style.display = 'none';
      document.querySelector('#compose-recipients').value = email.sender;
      if (!email.subject.startsWith('Re:')) {
        document.querySelector('#compose-subject').value = `Re: ${email.subject}`;
      } else {
        document.querySelector('#compose-subject').value = email.subject;
      }
      document.querySelector('#compose-body').value = `\nOn ${email.timestamp} ${email.sender} wrote: ${email.body}`;
  });
}

function delete_email(id) {
  fetch(`/emails/${id}`, {
    method: 'DELETE',
  })
  .then(() => load_mailbox('inbox'));
}
