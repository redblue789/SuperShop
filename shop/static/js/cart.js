let cart = [];

function addToCart(item) {
    cart.push(item);

    const cartCount = document.getElementById('cart-count');
    cartCount.innerText = cart.length;

    cartCount.classList.add('bounce');
    setTimeout(() => cartCount.classList.remove('bounce'), 500);

    const list = document.getElementById('cart-items');
    const li = document.createElement('li');
    li.innerText = item;
    list.appendChild(li);
}

function toggleCart() {
    document.getElementById('cart-panel').classList.toggle('open');
}

function filterProducts(category, element) {
    document.querySelectorAll('.tab').forEach(tab => tab.classList.remove('active'));
    element.classList.add('active');

    document.querySelectorAll('.card').forEach(card => {
        if (category === 'all' || card.dataset.category === category) {
            card.style.display = 'flex';
        } else {
            card.style.display = 'none';
        }
    });
}
