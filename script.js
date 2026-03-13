// ========== Nut Data ==========
const nutsData = {
    almond: {
        name: '아몬드', icon: '🥜',
        origin: '미국, 호주, 스페인',
        desc: '비타민E가 풍부하여 피부 건강과 항산화 효과가 뛰어납니다. 마그네슘이 풍부해 근육 이완과 스트레스 해소에 도움을 줍니다. 식이섬유가 풍부해 포만감이 오래 지속됩니다.',
        benefits: ['피부 건강 및 항산화', '혈당 조절 도움', '뼈 건강 (칼슘 풍부)', '콜레스테롤 개선'],
        intake: '23알', intakeGrams: '약 30g',
        calories: 579, protein: 21.2, fat: 49.9, carbs: 21.6, fiber: 12.5,
        vitaminE: 25.6, magnesium: 270, calcium: 269, iron: 3.7,
        price: 3500, color: '#f59e0b'
    },
    walnut: {
        name: '호두', icon: '🧠',
        origin: '미국, 중국, 칠레',
        desc: '오메가3 지방산(ALA)이 견과류 중 가장 풍부합니다. 뇌의 모양과 닮은 호두는 실제로 두뇌 건강에 탁월한 효능이 있으며, 기억력과 인지 기능 향상에 도움을 줍니다.',
        benefits: ['두뇌 건강 및 기억력 향상', '심혈관 질환 예방', '항염증 효과', '수면의 질 개선 (멜라토닌)'],
        intake: '7~8알', intakeGrams: '약 30g',
        calories: 654, protein: 15.2, fat: 65.2, carbs: 13.7, fiber: 6.7,
        vitaminE: 0.7, magnesium: 158, calcium: 98, iron: 2.9,
        price: 4200, color: '#8b5cf6'
    },
    cashew: {
        name: '캐슈넛', icon: '🌰',
        origin: '베트남, 인도, 브라질',
        desc: '부드럽고 달콤한 맛이 특징인 캐슈넛은 철분과 구리가 풍부하여 빈혈 예방에 효과적입니다. 견과류 중 칼로리가 비교적 낮아 다이어트 시에도 적당량 섭취 가능합니다.',
        benefits: ['빈혈 예방 (철분·구리)', '면역력 강화', '뼈·치아 건강', '포만감 유지 (다이어트)'],
        intake: '15~18알', intakeGrams: '약 30g',
        calories: 553, protein: 18.2, fat: 43.8, carbs: 30.2, fiber: 3.3,
        vitaminE: 0.9, magnesium: 292, calcium: 37, iron: 6.7,
        price: 3800, color: '#10b981'
    },
    macadamia: {
        name: '마카다미아', icon: '⚪',
        origin: '호주, 하와이, 남아프리카',
        desc: '견과류의 여왕이라 불리는 마카다미아는 올레산(단일불포화지방산)이 가장 풍부합니다. 크리미한 식감과 고소한 맛이 특징이며, 심혈관 건강에 특히 좋습니다.',
        benefits: ['심혈관 건강 (올레산)', 'LDL 콜레스테롤 감소', '항산화 효과', '피부 보습 효과'],
        intake: '10~12알', intakeGrams: '약 30g',
        calories: 718, protein: 7.9, fat: 75.8, carbs: 13.8, fiber: 8.6,
        vitaminE: 0.5, magnesium: 130, calcium: 85, iron: 3.7,
        price: 6500, color: '#f472b6'
    },
    pistachio: {
        name: '피스타치오', icon: '💚',
        origin: '이란, 미국, 터키',
        desc: '껍질을 까먹는 재미가 있는 피스타치오는 루테인과 제아잔틴이 풍부해 눈 건강에 특히 좋습니다. 비타민B6 함량이 견과류 중 최고 수준이며, 혈당 조절에도 효과적입니다.',
        benefits: ['눈 건강 (루테인·제아잔틴)', '혈당 조절', '비타민B6 최다 함유', '체중 관리 (껍질 까먹는 시간)'],
        intake: '49알', intakeGrams: '약 30g',
        calories: 560, protein: 20.2, fat: 45.3, carbs: 27.2, fiber: 10.6,
        vitaminE: 2.9, magnesium: 121, calcium: 105, iron: 3.9,
        price: 4500, color: '#22c55e'
    },
    peanut: {
        name: '땅콩', icon: '🥜',
        origin: '국내산, 중국, 미국',
        desc: '엄밀히는 콩과 식물이지만 견과류로 분류되는 땅콩은 단백질 함량이 가장 높습니다. 가격 대비 영양가가 우수하며, 나이아신(비타민B3)이 풍부해 에너지 대사에 도움을 줍니다.',
        benefits: ['근육 생성 (고단백)', '에너지 대사 (나이아신)', '포만감 제공', '가성비 최고의 견과류'],
        intake: '20~25알', intakeGrams: '약 30g',
        calories: 567, protein: 25.8, fat: 49.2, carbs: 16.1, fiber: 8.5,
        vitaminE: 8.3, magnesium: 168, calcium: 92, iron: 4.6,
        price: 1500, color: '#ef4444'
    },
    brazil: {
        name: '브라질너트', icon: '🌿',
        origin: '브라질, 볼리비아, 페루',
        desc: '셀레늄 함량이 압도적으로 높아 하루 1~2알이면 일일 권장량을 충족합니다. 갑상선 호르몬 대사에 필수적인 미네랄을 공급하며, 강력한 항산화 효과를 제공합니다.',
        benefits: ['갑상선 건강 (셀레늄)', '강력한 항산화 효과', '면역 기능 강화', '심혈관 보호'],
        intake: '1~2알', intakeGrams: '약 5~10g',
        calories: 659, protein: 14.3, fat: 67.1, carbs: 11.7, fiber: 7.5,
        vitaminE: 5.7, magnesium: 376, calcium: 160, iron: 2.4,
        price: 7000, color: '#14b8a6'
    },
    hazelnut: {
        name: '헤이즐넛', icon: '🤎',
        origin: '터키, 이탈리아, 미국',
        desc: '초콜릿과의 궁합이 최고인 헤이즐넛은 비타민E와 올레산이 풍부합니다. 피부 노화 방지와 혈관 건강에 좋으며, 엽산이 풍부해 임산부에게도 추천되는 견과류입니다.',
        benefits: ['피부 노화 방지 (비타민E)', '혈관 건강 (올레산)', '엽산 풍부 (임산부 추천)', '뼈 건강 (망간)'],
        intake: '20알', intakeGrams: '약 30g',
        calories: 628, protein: 15.0, fat: 60.8, carbs: 16.7, fiber: 9.7,
        vitaminE: 15.0, magnesium: 163, calcium: 114, iron: 4.7,
        price: 4000, color: '#a855f7'
    }
};

const nutOrder = ['almond', 'walnut', 'cashew', 'macadamia', 'pistachio', 'peanut', 'brazil', 'hazelnut'];

const chartDataMap = {
    calories: { key: 'calories', unit: 'kcal', label: '칼로리 (kcal)' },
    protein: { key: 'protein', unit: 'g', label: '단백질 (g)' },
    fat: { key: 'fat', unit: 'g', label: '지방 (g)' },
    fiber: { key: 'fiber', unit: 'g', label: '식이섬유 (g)' },
    vitaminE: { key: 'vitaminE', unit: 'mg', label: '비타민E (mg)' }
};

const barGradients = [
    'linear-gradient(90deg, #f59e0b, #f97316)',
    'linear-gradient(90deg, #8b5cf6, #6366f1)',
    'linear-gradient(90deg, #10b981, #14b8a6)',
    'linear-gradient(90deg, #f472b6, #ec4899)',
    'linear-gradient(90deg, #22c55e, #16a34a)',
    'linear-gradient(90deg, #ef4444, #dc2626)',
    'linear-gradient(90deg, #14b8a6, #0d9488)',
    'linear-gradient(90deg, #a855f7, #9333ea)'
];

// ========== Bar Chart ==========
function renderBarChart(chartType) {
    const chart = document.getElementById('barChart');
    const unitEl = document.getElementById('chartUnit');
    const data = chartDataMap[chartType];

    const values = nutOrder.map(k => nutsData[k][data.key]);
    const maxVal = Math.max(...values);

    unitEl.textContent = `단위: ${data.label} (100g 기준)`;

    chart.innerHTML = nutOrder.map((key, i) => {
        const nut = nutsData[key];
        const val = nut[data.key];
        const pct = (val / maxVal) * 100;
        return `
            <div class="bar-row fade-in">
                <span class="bar-label">${nut.name}</span>
                <div class="bar-track">
                    <div class="bar-fill" style="width:0%;background:${barGradients[i]}" data-width="${pct}%"></div>
                </div>
                <span class="bar-value">${val}</span>
            </div>
        `;
    }).join('');

    requestAnimationFrame(() => {
        requestAnimationFrame(() => {
            chart.querySelectorAll('.bar-fill').forEach(el => {
                el.style.width = el.dataset.width;
            });
            chart.querySelectorAll('.fade-in').forEach((el, i) => {
                setTimeout(() => el.classList.add('visible'), i * 60);
            });
        });
    });
}

// ========== Detail Panel ==========
function renderDetail(nutKey) {
    const nut = nutsData[nutKey];
    document.getElementById('detailIcon').textContent = nut.icon;
    document.getElementById('detailName').textContent = nut.name;
    document.getElementById('detailOrigin').textContent = `원산지: ${nut.origin}`;
    document.getElementById('detailDesc').textContent = nut.desc;
    document.getElementById('intakeAmount').textContent = nut.intake;
    document.getElementById('intakeGrams').textContent = `(${nut.intakeGrams})`;

    const benefitsUl = document.querySelector('#detailBenefits ul');
    benefitsUl.innerHTML = nut.benefits.map(b => `<li>${b}</li>`).join('');

    const nutrients = [
        { name: '단백질', value: nut.protein, unit: 'g', max: 30, color: '#ec4899' },
        { name: '지방', value: nut.fat, unit: 'g', max: 80, color: '#f59e0b' },
        { name: '탄수화물', value: nut.carbs, unit: 'g', max: 35, color: '#3b82f6' },
        { name: '식이섬유', value: nut.fiber, unit: 'g', max: 15, color: '#10b981' },
        { name: '비타민E', value: nut.vitaminE, unit: 'mg', max: 30, color: '#f97316' },
        { name: '마그네슘', value: nut.magnesium, unit: 'mg', max: 400, color: '#8b5cf6' },
        { name: '칼슘', value: nut.calcium, unit: 'mg', max: 300, color: '#14b8a6' },
        { name: '철분', value: nut.iron, unit: 'mg', max: 8, color: '#ef4444' }
    ];

    const barsContainer = document.getElementById('nutrientBars');
    barsContainer.innerHTML = nutrients.map(n => {
        const pct = Math.min((n.value / n.max) * 100, 100);
        return `
            <div class="nutrient-row">
                <div class="nutrient-info">
                    <span class="nutrient-name">${n.name}</span>
                    <span class="nutrient-value">${n.value}${n.unit}</span>
                </div>
                <div class="nutrient-track">
                    <div class="nutrient-fill" style="width:0%;background:${n.color}" data-width="${pct}%"></div>
                </div>
            </div>
        `;
    }).join('');

    requestAnimationFrame(() => {
        requestAnimationFrame(() => {
            barsContainer.querySelectorAll('.nutrient-fill').forEach(el => {
                el.style.width = el.dataset.width;
            });
        });
    });
}

// ========== Price Chart ==========
function renderPriceChart() {
    const container = document.getElementById('priceChart');
    const prices = nutOrder.map(k => nutsData[k].price);
    const maxPrice = Math.max(...prices);

    container.innerHTML = nutOrder.map((key, i) => {
        const nut = nutsData[key];
        const pct = (nut.price / maxPrice) * 100;
        return `
            <div class="price-item fade-in">
                <div class="price-value">${(nut.price).toLocaleString()}원</div>
                <div class="price-bar-container">
                    <div class="price-bar" style="height:0%;background:${barGradients[i]}" data-height="${pct}%"></div>
                </div>
                <div class="price-name">${nut.name}</div>
            </div>
        `;
    }).join('');

    requestAnimationFrame(() => {
        requestAnimationFrame(() => {
            container.querySelectorAll('.price-bar').forEach(el => {
                el.style.height = el.dataset.height;
            });
        });
    });
}

// ========== Scroll Animation ==========
function setupScrollAnimation() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, { threshold: 0.1 });

    document.querySelectorAll('.nut-card, .best-card, .tip-card, .price-item').forEach(el => {
        el.classList.add('fade-in');
        observer.observe(el);
    });
}

// ========== Event Listeners ==========
document.addEventListener('DOMContentLoaded', () => {
    // Chart tabs
    renderBarChart('calories');
    document.querySelectorAll('.chart-tab').forEach(tab => {
        tab.addEventListener('click', () => {
            document.querySelectorAll('.chart-tab').forEach(t => t.classList.remove('active'));
            tab.classList.add('active');
            renderBarChart(tab.dataset.chart);
        });
    });

    // Detail selector
    renderDetail('almond');
    document.querySelectorAll('.detail-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            document.querySelectorAll('.detail-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            renderDetail(btn.dataset.detail);
        });
    });

    // Price chart
    renderPriceChart();

    // Scroll animations
    setupScrollAnimation();

    // Intersection observer for price chart animation
    const priceSection = document.querySelector('.price-section');
    const priceObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                document.querySelectorAll('.price-bar').forEach(el => {
                    el.style.height = el.dataset.height;
                });
                document.querySelectorAll('.price-item.fade-in').forEach((el, i) => {
                    setTimeout(() => el.classList.add('visible'), i * 80);
                });
            }
        });
    }, { threshold: 0.2 });
    if (priceSection) priceObserver.observe(priceSection);
});
