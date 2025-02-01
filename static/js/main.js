// Função que faz o número de itens do carrinho ser dinâmico de acordo com o que o cliente adicionar 
document.addEventListener("DOMContentLoaded", function () {
    const cartCountElement = document.getElementById("cart-count");
    const buyButton = document.querySelector(".btn-add-cart");
    const quantityInput = document.getElementById("quantity");

    if (buyButton && cartCountElement && quantityInput) {
        buyButton.addEventListener("click", function () {
        let currentCount = parseInt(cartCountElement.textContent);
        let selectedQuantity = parseInt(quantityInput.value);

        cartCountElement.textContent = currentCount + selectedQuantity;
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


