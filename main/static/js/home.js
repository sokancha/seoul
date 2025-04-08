const slider = document.getElementById('slider');
const dotsContainer = document.getElementById('dots');
const slides = document.querySelectorAll('.slide');

const titles = [
  "낭만이 가득한 여행",
  "벚꽃이 피는 4월",
  "해가 지면 더 멋있는 장소"
];

const descriptions = [
  ["1-1 설명",
    `<a href="/trip_course/" style="color:rgb(0, 6, 12); text-decoration: none;">자세히 보기</a>`
  ],
  ["2-1설명",
    `<a href="/flower_place/" style="color:rgb(0, 6, 12); text-decoration: none;">자세히 보기</a>`
  ],
  ["3-1설명",
    `<a href="/night_place/" style="color: rgb(0, 6, 12); text-decoration: none;">자세히 보기</a>`
  ]
];

const titleEl = document.getElementById("title");
const desc1El = document.getElementById("desc1");
const desc2El = document.getElementById("desc2");

let currentIndex = 0;

function updateText(index) {
  titleEl.textContent = titles[index];
  desc1El.textContent = descriptions[index][0];
  desc2El.innerHTML = descriptions[index][1];
}

function goToSlide(index) {
  currentIndex = index;
  slider.style.transform = `translateX(-${index * 100}%)`;
  updateDots();
  updateText(index);
}

function createDots() {
  slides.forEach((_, index) => {
    const dot = document.createElement('div');
    dot.classList.add('dot');
    if (index === 0) dot.classList.add('active');
    dot.addEventListener('click', () => goToSlide(index));
    dotsContainer.appendChild(dot);
  });
}

function updateDots() {
  document.querySelectorAll('.dot').forEach((dot, i) => {
    dot.classList.toggle('active', i === currentIndex);
  });
}

function nextSlide() {
  currentIndex = (currentIndex + 1) % slides.length;
  goToSlide(currentIndex);
}

createDots();
updateText(0);
setInterval(nextSlide, 4000);
