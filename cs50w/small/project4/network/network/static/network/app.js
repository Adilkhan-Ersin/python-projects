// Get CSRF token
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}

// Edit post
function submitHandler(id) {
  const textarea = document.getElementById(`textarea_${id}`).value;
  const content = document.getElementById(`post_${id}`);
  const modal = document.getElementById(`editModal${id}`);
  const csrftoken = getCookie('csrftoken');

  if (!csrftoken) {
    console.error('CSRF token not found');
    return;
  }

  fetch(`/edit/${id}`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrftoken,
    },
    body: JSON.stringify({
      content: textarea
    }),
  })
  .then(response => response.json())
  .then(result => {
    content.innerHTML = result.data;
    modal.classList.remove('show');
    modal.setAttribute('aria-hidden', 'true');
    modal.setAttribute('style', 'display: none;');
    const modalsBack = document.getElementsByClassName('modal-backdrop');
    for (let i = 0; i < modalsBack.length; i++) {
      document.body.removeChild(modalsBack[i]);
    }
  })
  .catch(error => {
    console.error('Error:', error);
  });
}

// Like post
like = document.querySelectorAll(".liked");
like.forEach((element) => {
  like_handeler(element);
});

function like_handeler(element) {
  element.addEventListener("click", () => {
    id = element.getAttribute("data-id");
    is_liked = element.getAttribute("data-is_liked");
    icon = document.querySelector(`#post-like-${id}`);
    count = document.querySelector(`#post-count-${id}`);

    form = new FormData();
    form.append("id", id);
    form.append("is_liked", is_liked);
    fetch("/like/", {
      method: "POST",
      body: form,
    })
      .then((res) => res.json())
      .then((res) => {
        if (res.status == 201) {
          if (res.is_liked === "true") {
            icon.className = "liked bi bi-heart-fill";
            element.setAttribute("data-is_liked", "true");
          } else {
            icon.className = "liked bi bi-heart";
            element.setAttribute("data-is_liked", "false");
          }
          count.textContent = res.like_count;
        }
      })
      .catch(function (res) {
        alert("Network Error. Please Check your connection.");
      });
  });
}