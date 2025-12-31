/* ========================================
   MANWELL - JavaScript Interactivity
   ======================================== */

// ========== MOBILE MENU TOGGLE ==========
const menuToggle = document.querySelector('.menu-toggle');
const nav = document.querySelector('nav ul');

if (menuToggle) {
  menuToggle.addEventListener('click', () => {
    nav.classList.toggle('active');
  });

  // Close menu when link is clicked
  document.querySelectorAll('nav a').forEach(link => {
    link.addEventListener('click', () => {
      nav.classList.remove('active');
    });
  });
}

// ========== REVEAL ON SCROLL ==========
const revealElements = document.querySelectorAll('.reveal');

const observerOptions = {
  threshold: 0.1,
  rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('active');
      observer.unobserve(entry.target);
    }
  });
}, observerOptions);

revealElements.forEach(element => {
  observer.observe(element);
});

// ========== SMOOTH SCROLL ANCHOR LINKS ==========
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    const href = this.getAttribute('href');
    if (href !== '#') {
      e.preventDefault();
      const target = document.querySelector(href);
      if (target) {
        target.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
      }
    }
  });
});

// ========== FORM SUBMISSION HANDLING ==========
const form = document.getElementById('newsletter-form');

if (form) {
  form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const formData = new FormData(form);
    const name = formData.get('name');
    const email = formData.get('email');

    // Validate email
    if (!email || !email.includes('@')) {
      alert('Please enter a valid email address.');
      return;
    }

    // TODO: Replace with your actual API endpoint
    // This is a placeholder for Mailchimp or ConvertKit integration
    console.log('Newsletter signup:', { name, email });

    // Show confirmation
    form.style.display = 'none';
    const confirmation = document.createElement('div');
    confirmation.className = 'form-confirmation';
    confirmation.innerHTML = `
      <h3>Welcome to the Séance.</h3>
      <p>Check your email for the first message. It arrives at dawn.</p>
    `;
    form.parentElement.appendChild(confirmation);
  });
}

// ========== LAZY LOAD IMAGES ==========
if ('IntersectionObserver' in window) {
  const lazyImages = document.querySelectorAll('img[data-src]');
  const imageObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const img = entry.target;
        img.src = img.dataset.src;
        img.classList.add('loaded');
        observer.unobserve(img);
      }
    });
  });

  lazyImages.forEach(img => imageObserver.observe(img));
}

// ========== HEADER SCROLL EFFECT ==========
let lastScrollTop = 0;
const header = document.querySelector('header');

window.addEventListener('scroll', () => {
  let scrollTop = window.pageYOffset || document.documentElement.scrollTop;

  if (scrollTop > 100) {
    header.style.borderBottomColor = 'rgba(255, 90, 9, 0.3)';
  } else {
    header.style.borderBottomColor = 'rgba(255, 255, 255, 0.1)';
  }

  lastScrollTop = scrollTop <= 0 ? 0 : scrollTop;
});

// ========== PARALLAX EFFECT FOR HERO ==========
const hero = document.querySelector('.hero');
if (hero) {
  window.addEventListener('scroll', () => {
    const scrollPosition = window.pageYOffset;
    const heroVideo = document.querySelector('.hero-video');
    if (heroVideo) {
      heroVideo.style.transform = `translateY(${scrollPosition * 0.5}px)`;
    }
  });
}

// ========== SOCIAL LINK ANIMATION ==========
document.querySelectorAll('.social-link').forEach(link => {
  link.addEventListener('mouseenter', function() {
    this.style.transform = 'translateY(-3px)';
  });

  link.addEventListener('mouseleave', function() {
    this.style.transform = 'translateY(0)';
  });
});

// ========== UTILITY: DARK MODE TOGGLE (OPTIONAL) ==========
// Uncomment if implementing dark/light mode toggle
/*
const toggleDarkMode = () => {
  document.body.classList.toggle('light-mode');
  localStorage.setItem('darkMode', document.body.classList.contains('light-mode') ? 'false' : 'true');
};

if (localStorage.getItem('darkMode') === 'false') {
  document.body.classList.add('light-mode');
}
*/

console.log('Manwell is loaded. Father yourself.');
