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

// Edit Goal function
function editGoal(goalId) {
  const goalName = document.getElementById(`goal_name_${goalId}`).value;
  const goalAmount = document.getElementById(`goal_amount_${goalId}`).value;
  const modal = document.getElementById(`editGoal${goalId}`);
  const csrftoken = getCookie('csrftoken');

  if (!goalAmount || isNaN(parseInt(goalAmount))) {
    alert("Please enter a valid number for the amount.");
    return;
  }

  if (!goalName || goalName.trim() === '') {
    alert("Please fill out name field.");
    return;
  }

  fetch(`/edit_goal/${goalId}`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrftoken,
    },
    body: JSON.stringify({
      content: goalName,
      goal_amount: parseInt(goalAmount)
    }),
  })
  .then(response => response.json())
  .then(result => {
    if (result.message === "Success") {
      // Update the UI with the new content
      document.getElementById(`goal_name_${goalId}`).innerHTML = result.data.content;
      document.getElementById(`goal_amount_${goalId}`).innerHTML = result.data.goal_amount;

      // Close the modal after saving
      const bootstrapModal = bootstrap.Modal.getInstance(modal);
      bootstrapModal.hide();
      location.reload();
    } else {
      alert(result.message);
    }
  })
  .catch(error => {
    console.error('Error:', error);
  });
}

// Delete Goal function
function deleteGoal(goalId) {
  const modal = document.getElementById(`deleteGoal${goalId}`);
  const csrftoken = getCookie('csrftoken');

  fetch(`/delete_goal/${goalId}`, {
      method: "POST",
      headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrftoken
      },
  })
  .then(response => response.json())
  .then(result => {
      if (result.message === "Success") {
          // Remove the goal from the DOM
          const goalElement = document.getElementById(`goal-${goalId}`);
          if (goalElement) {
              goalElement.remove();
          }

          // Close the modal after successful deletion
          const bootstrapModal = bootstrap.Modal.getInstance(modal);
          bootstrapModal.hide();
      } else {
          alert(result.error || "Error deleting goal.");
      }
  });
}