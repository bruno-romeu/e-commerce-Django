// Função que faz o número de itens do carrinho ser dinâmico de acordo com o que o cliente adicionar 
document.addEventListener("DOMContentLoaded", function () {
    const cartCountElement = document.getElementById("cart-count");
    const buyButton = document.querySelector(".btn-add-cart");
    const quantityInput = document.getElementById("quantity");

    // Recupera o número total de itens do localStorage ou define como 0 se não existir
    let totalItems = parseInt(localStorage.getItem("totalItems")) || 0;

    // Atualiza o contador dinâmico ao carregar a página
    if (cartCountElement) {
        cartCountElement.textContent = totalItems;
    }

    if (buyButton && cartCountElement && quantityInput) {
        buyButton.addEventListener("click", function () {
            let selectedQuantity = parseInt(quantityInput.value);

            // Atualiza o número total de itens
            totalItems += selectedQuantity;

            // Salva o número total de itens no localStorage
            localStorage.setItem("totalItems", totalItems);

            // Atualiza o contador dinâmico
            cartCountElement.textContent = totalItems;
        });
    }
});


// Função que configura o botão que seleciona a quantidade de produtos no detail.html
function updateQuantity(change) {
    const quantityInput = document.getElementById('quantity');
    let currentQuantity = parseInt(quantityInput.value);

    if (!isNaN(currentQuantity)) {
        currentQuantity += change;
        if (currentQuantity < 1) currentQuantity = 1; // Não permitir valores menores que 1
        quantityInput.value = currentQuantity;
    }
    }


//Função que envia as informações do formulário de contato para o banco de dados
function enviarFormulario() {
    var dadosFormulario = $('#meuForm').serialize();

    $.ajax({
        type: 'POST',
        url: '/enviar_formulario/',
        data: dadosFormulario,
        success: function(response) {
            $('#meuForm').trigger('reset'); 
            $('.bd-example-modal-lg').modal('show');
        },
        error: function(error) {
            console.error("Erro ao enviar os dados:", error);
        }
    });
}


//Função que abre o modal de ero ao calcular o frete somente quando realmente acontece algum erro.
document.addEventListener("DOMContentLoaded", function() {
    var modalErro = document.getElementById('staticBackdrop');
    
    if (modalErro && modalErro.dataset.show === "true") {
        var bootstrapModal = new bootstrap.Modal(modalErro);
        bootstrapModal.show();
    }
});

//Função que controla os intens do sidebar de carrinho na página detail.hmtl
document.addEventListener("DOMContentLoaded", function () {
    let cart = JSON.parse(localStorage.getItem("cart")) || [];
    updateCartDisplay();
    updateTotalItems();

    document.querySelector(".btn-add-cart").addEventListener("click", function () {
        let productId = this.getAttribute('data-product-id');
        let productName = this.getAttribute('data-product-name');
        let productPrice = parseFloat(this.getAttribute('data-product-price'));
        let quantity = parseInt(document.getElementById("quantity").value);
        if (isNaN(quantity) || quantity < 1) {
            alert("Por favor, insira uma quantidade válida.");
            return;
        }
        let essence = document.getElementById("tamanho").options[document.getElementById("tamanho").selectedIndex].text;
        let photo = this.getAttribute('data-product-photo')

        let existingProduct = cart.find(item => item.id === productId && item.essence === essence);
        if (existingProduct) {
            existingProduct.quantity += quantity;
        } else {
            cart.push({ 
                id: productId, 
                name: productName, 
                price: productPrice, 
                quantity: quantity, 
                essence: essence, 
                image: photo 
            });
        }

        localStorage.setItem("cart", JSON.stringify(cart)); 
        updateCartDisplay(); 
        updateTotalItems(); 
    });

    function updateCartDisplay() {
        let cartDisplay = document.querySelector(".offcanvas-body");
        cartDisplay.innerHTML = ""; 
    
        if (cart.length === 0) {
            cartDisplay.innerHTML = `<p class="empty-cart-message">Nenhum item adicionado ao carrinho.</p>`;
        } else {
            cart.forEach((item, index) => {
                cartDisplay.innerHTML += `
                    <div class="cart-item">
                        <img class="foto-prod-cart" src="${item.image}" alt="${item.name}">
                        <div class="text-cart">
                            <p>${item.name}</p>
                            <p>(${item.essence}) - ${item.quantity}x </p>
                            <p>R$${(item.price.toFixed(2)).replace('.', ',')}</p>
                        </div>
                        <button class="btn-remove-item" data-index="${index}">X</button>
                    </div>
                `;
            });
        }
    
        addRemoveItemListeners(); 
    }

    function addRemoveItemListeners() {
        const removeButtons = document.querySelectorAll(".btn-remove-item");

        removeButtons.forEach(button => {
            button.addEventListener("click", function () {
                const index = parseInt(button.getAttribute("data-index")); 

                cart.splice(index, 1);

                localStorage.setItem("cart", JSON.stringify(cart));
                updateCartDisplay(); 
                updateTotalItems(); 
            });
        });
    }

    function updateTotalItems() {
        const cartCountElement = document.getElementById("cart-count");

        if (cartCountElement) {
            let totalItems = cart.reduce((total, item) => total + item.quantity, 0);

            cartCountElement.textContent = totalItems;

            localStorage.setItem("totalItems", totalItems);
        }
    }
});