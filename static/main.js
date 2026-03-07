// Main JavaScript for ENNARQ Site

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      target.scrollIntoView({
        behavior: 'smooth',
        block: 'start'
      });
    }
  });
});

// Auto-close alerts after 5 seconds
document.addEventListener('DOMContentLoaded', function() {
  const alerts = document.querySelectorAll('.alert');
  alerts.forEach(alert => {
    setTimeout(() => {
      alert.style.animation = 'slideOut 0.3s ease';
      setTimeout(() => alert.remove(), 300);
    }, 5000);
  });
});

// Crane animation (placeholder for future implementation)
// This will be enhanced in a future phase with actual crane SVG and mouse tracking
const craneContainer = document.getElementById('crane-container');
if (craneContainer) {
  // Placeholder for crane animation
  // Will track mouse position and create pull animation on click
}

// Form validation helpers
function validateCPF(cpf) {
  cpf = cpf.replace(/\D/g, '');
  if (cpf.length !== 11) return false;
  
  // Check if all digits are the same
  if (/^(\d)\1{10}$/.test(cpf)) return false;
  
  return true;
}

function validateCNPJ(cnpj) {
  cnpj = cnpj.replace(/\D/g, '');
  if (cnpj.length !== 14) return false;
  
  // Check if all digits are the same
  if (/^(\d)\1{13}$/.test(cnpj)) return false;
  
  return true;
}

// Export functions for use in other scripts
window.ENNARQ = {
  validateCPF,
  validateCNPJ
};
