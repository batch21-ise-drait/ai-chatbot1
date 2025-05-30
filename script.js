// Toggle chat visibility (if needed in future)
function toggleChat() {
  const chat = document.getElementById('chatContainer');
  if (chat.style.display === 'block') {
    chat.style.display = 'none';
  } else {
    chat.style.display = 'block';
  }
}

// Smooth scrolling for nav links
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll('nav ul li a').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      const targetID = this.getAttribute('href').substring(1);
      const targetSection = document.getElementById(targetID);
      if (targetSection) {
        window.scrollTo({
          top: targetSection.offsetTop - 60,
          behavior: 'smooth'
        });
      }
    });
  });
});
