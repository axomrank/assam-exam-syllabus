// =========================================================
// AxomRank — JavaScript Engine (axomrank.web.app)
// Preview Beta Interaction, Navigation & Syllabus Search
// =========================================================

let currentScreen = 1;
let currentViewMode = 'gallery'; // 'gallery' | 'app'
let currentScore = 12;
let maxCards = 20;
let syllabusData = null;
let currentDomainFilter = 'All';

// Templates of the 5 screens for the interactive single phone simulator
const screenTemplates = {};

document.addEventListener('DOMContentLoaded', () => {
  // Cache the inner HTML of the 5 screens from the gallery
  for (let i = 1; i <= 5; i++) {
    const col = document.querySelector(`.phone-column:nth-child(${i}) .phone-chassis`);
    if (col) {
      screenTemplates[i] = col.innerHTML;
    }
  }

  // Check screen width: if mobile, default to app mode
  if (window.innerWidth <= 768) {
    switchView('app');
  } else {
    switchView('gallery');
  }

  // Load Syllabus JSON
  loadSyllabus();

  // Initialize confetti canvas size
  setupConfetti();
});

// View mode switcher: 'gallery' (5-stage panorama) vs 'app' (single phone)
function switchView(mode) {
  currentViewMode = mode;
  const galleryEl = document.getElementById('galleryView');
  const appEl = document.getElementById('appView');
  const btnGallery = document.getElementById('btnGalleryMode');
  const btnApp = document.getElementById('btnAppMode');

  if (mode === 'gallery') {
    galleryEl.style.display = 'block';
    appEl.style.display = 'none';
    btnGallery.classList.add('active');
    btnApp.classList.remove('active');
  } else {
    galleryEl.style.display = 'none';
    appEl.style.display = 'flex';
    btnGallery.classList.remove('active');
    btnApp.classList.add('active');
    renderSimulatorScreen(currentScreen);
  }
}

// Select a journey step from top nav or controls
function selectJourneyStep(stepNum) {
  showScreen(stepNum);
  if (currentViewMode === 'gallery') {
    // Scroll the phone into view
    const col = document.querySelectorAll('.phone-column')[stepNum - 1];
    if (col) {
      col.scrollIntoView({ behavior: 'smooth', inline: 'center', block: 'nearest' });
    }
  }
}

// Show specific screen (1..5)
function showScreen(num) {
  currentScreen = num;

  // Update top stepper
  document.querySelectorAll('.stepper-nav .step-btn').forEach(btn => {
    btn.classList.toggle('active', parseInt(btn.dataset.step) === num);
  });

  // Update simulator pill controls
  document.querySelectorAll('.sim-pill').forEach((btn, idx) => {
    btn.classList.toggle('active', (idx + 1) === num);
  });

  // If in simulator app mode, re-render
  if (currentViewMode === 'app') {
    renderSimulatorScreen(num);
  }
}

function renderSimulatorScreen(num) {
  const chassis = document.getElementById('simulatorChassis');
  if (chassis && screenTemplates[num]) {
    chassis.innerHTML = screenTemplates[num];
  }
}

// Flashcard interactions
function flipFlashcard() {
  const fc = document.getElementById('flashcardElement');
  if (fc) {
    fc.style.transform = 'scale(0.98)';
    setTimeout(() => {
      fc.style.transform = 'scale(1)';
    }, 150);
  }
}

function knowFlashcard() {
  if (currentScore < maxCards) {
    currentScore++;
  }
  updateFlashcardScore();
  triggerMiniToast('Card Mastered! +10 XP');
}

function reviseFlashcard() {
  triggerMiniToast('Added to Spaced Repetition queue');
  flipFlashcard();
}

function nextFlashcard() {
  triggerMiniToast('Next bite-sized card loaded');
  flipFlashcard();
}

function updateFlashcardScore() {
  const disp = document.getElementById('flashcardScoreDisplay');
  if (disp) {
    disp.textContent = `${currentScore}/${maxCards}`;
  }
  const fill = document.querySelector('.circle-fill');
  if (fill) {
    const percent = Math.round((currentScore / maxCards) * 100);
    fill.setAttribute('stroke-dasharray', `${percent}, 100`);
  }
}

// Quiz Interactions
function selectOption(letter) {
  const container = document.getElementById('quizOptionsContainer');
  const exp = document.getElementById('quizExplanation');
  if (!container) return;

  const pills = container.querySelectorAll('.option-pill');
  pills.forEach(p => p.classList.remove('correct', 'wrong'));

  if (letter === 'A') {
    const optA = document.getElementById('optA');
    if (optA) {
      optA.classList.add('correct');
      if (exp) exp.style.display = 'block';
    }
    triggerConfetti(0.4);
  } else {
    const chosen = document.getElementById(`opt${letter}`);
    if (chosen) {
      chosen.classList.add('wrong');
      chosen.style.borderColor = '#EF4444';
      chosen.style.background = '#FEF2F2';
      setTimeout(() => {
        chosen.style.borderColor = '';
        chosen.style.background = '';
      }, 800);
    }
  }
}

// Celebration when finishing Match & Complete
function celebrateAndLoop() {
  triggerConfetti(1.0);
  setTimeout(() => {
    switchView('app');
    showScreen(1);
    triggerMiniToast('Starting Next Topic: Assam Geography!');
  }, 1200);
}

// Mini Toast notification
function triggerMiniToast(msg) {
  const existing = document.getElementById('axomToast');
  if (existing) existing.remove();

  const toast = document.createElement('div');
  toast.id = 'axomToast';
  toast.style.cssText = `
    position: fixed;
    bottom: 24px;
    left: 50%;
    transform: translateX(-50%);
    background: #0F172A;
    color: #FFFFFF;
    font-size: 13px;
    font-weight: 700;
    padding: 10px 20px;
    border-radius: 9999px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.25);
    z-index: 3000;
    display: flex;
    align-items: center;
    gap: 8px;
    animation: toastIn 0.25s ease;
  `;
  toast.innerHTML = `<span>✨</span><span>${msg}</span>`;
  document.body.appendChild(toast);

  setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.transition = 'opacity 0.3s ease';
    setTimeout(() => toast.remove(), 300);
  }, 2200);
}

// Confetti Particle Physics
function setupConfetti() {
  const canvas = document.getElementById('confettiCanvas');
  if (!canvas) return;
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
  window.addEventListener('resize', () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  });
}

function triggerConfetti(intensity = 0.5) {
  const canvas = document.getElementById('confettiCanvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const count = Math.floor(100 * intensity);
  const colors = ['#D32F2F', '#16A34A', '#2563EB', '#F59E0B', '#8B5CF6', '#EC4899'];
  const particles = [];

  for (let i = 0; i < count; i++) {
    particles.push({
      x: window.innerWidth * 0.5 + (Math.random() * 200 - 100),
      y: window.innerHeight * 0.4,
      w: Math.random() * 8 + 4,
      h: Math.random() * 6 + 4,
      color: colors[Math.floor(Math.random() * colors.length)],
      vx: (Math.random() - 0.5) * 12,
      vy: -Math.random() * 12 - 4,
      rot: Math.random() * 360,
      rotSpeed: (Math.random() - 0.5) * 10,
      opacity: 1
    });
  }

  let animationFrame;
  function update() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    let active = false;

    particles.forEach(p => {
      p.x += p.vx;
      p.y += p.vy;
      p.vy += 0.35; // gravity
      p.rot += p.rotSpeed;
      p.opacity -= 0.012;

      if (p.opacity > 0) {
        active = true;
        ctx.save();
        ctx.globalAlpha = p.opacity;
        ctx.translate(p.x, p.y);
        ctx.rotate((p.rot * Math.PI) / 180);
        ctx.fillStyle = p.color;
        ctx.fillRect(-p.w / 2, -p.h / 2, p.w, p.h);
        ctx.restore();
      }
    });

    if (active) {
      animationFrame = requestAnimationFrame(update);
    } else {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      cancelAnimationFrame(animationFrame);
    }
  }
  update();
}

// ----------------------------------------------------
// SYLLABUS MODAL & LIVE SEARCH (842 Topics)
// ----------------------------------------------------
async function loadSyllabus() {
  try {
    const res = await fetch('assets/syllabus_summary.json');
    syllabusData = await res.json();
    renderSyllabusList();
  } catch (e) {
    console.warn('Syllabus load fallback:', e);
  }
}

function openSyllabusModal(domain = null) {
  const modal = document.getElementById('syllabusModal');
  if (modal) {
    modal.classList.add('open');
    if (domain) {
      filterByDomain(domain);
    } else {
      renderSyllabusList();
    }
  }
}

function closeSyllabusModal(e) {
  const modal = document.getElementById('syllabusModal');
  if (modal) {
    modal.classList.remove('open');
  }
}

function filterByDomain(domain) {
  currentDomainFilter = domain;
  document.querySelectorAll('.modal-domain-tabs .modal-tab').forEach(tab => {
    tab.classList.toggle('active', tab.textContent.includes(domain === 'All' ? 'All' : domain));
  });
  renderSyllabusList();
}

function filterSyllabus() {
  renderSyllabusList();
}

function renderSyllabusList() {
  const listEl = document.getElementById('modalTopicList');
  const countEl = document.getElementById('mfCount');
  const search = (document.getElementById('syllabusSearchInput')?.value || '').toLowerCase().trim();

  if (!listEl || !syllabusData) return;

  listEl.innerHTML = '';
  let count = 0;

  for (const [dom, dData] of Object.entries(syllabusData.domains)) {
    if (currentDomainFilter !== 'All' && currentDomainFilter !== dom) {
      continue;
    }

    for (const [subject, topics] of Object.entries(dData.subjects)) {
      for (const topic of topics) {
        if (search && !topic.toLowerCase().includes(search) && !subject.toLowerCase().includes(search) && !dom.toLowerCase().includes(search)) {
          continue;
        }

        count++;
        const card = document.createElement('div');
        card.className = 'syllabus-item-card';
        card.onclick = () => {
          closeSyllabusModal();
          triggerMiniToast(`Topic selected: ${topic}`);
          switchView('app');
          showScreen(2);
        };
        card.innerHTML = `
          <span class="sic-domain">${dom}</span>
          <span class="sic-subject">${subject}</span>
          <span class="sic-topic">${topic}</span>
        `;
        listEl.appendChild(card);
      }
    }
  }

  if (countEl) {
    countEl.textContent = `Showing ${count} atomic topics (${currentDomainFilter} domain)`;
  }
}
