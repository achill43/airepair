//MainMenu


var getInputOnlyNumber = (input ) => {
    // Функция удаляет все символы кроме цифр
    return input.value.trim().replace(/\D/g, "").substring(0, 12);
}
var checkFirstDigit = (phone) => {
    // Фуцкция проверяет первую цифру и добавляет недостающие стандартные цифры
    // перед ней
    if (phone[0] == "0") {
        phone = "38" + phone;
    }
    else if (phone[0] == "8") {
        phone = "3" + phone;
    }
    else if (phone[0] == "9") {
        phone = "380" + phone;
    }
    return phone;
}
var addMask = (phone) => {
    // Функция добавляет маску к номеру телефона
    let phone_with_mask = phone.substring(0, 2);
    if (phone.length > 2) {
        phone_with_mask += "(" + phone.substring(2, 5);
    }
    if (phone.length > 5) {
        phone_with_mask += ")-" + phone.substring(5, 8);
    }
    if (phone.length > 8) {
        phone_with_mask += "-" + phone.substring(8, 10);
    }
    if (phone.length > 10) {
        phone_with_mask += "-" + phone.substring(10, 12);
    }
    return "+" + phone_with_mask;
}

var phoneInput = (e) => {
    let input = e.target,
        inputValue = input.value,
        inputNumberValue = getInputOnlyNumber(input),
        cursorPointer = input.selectionStart;
    if (cursorPointer != inputValue.length) {
        // Убираем перемещение курсора в конец
        if (e.data && /\D/g.test(e.data)) {
            // Проверка если пользователь ввел чтото по мимо цифр в середину рядка
            inputNumberValue = getInputOnlyNumber(input);
            input.value = addMask(inputNumberValue);
            input.selectionStart = cursorPointer;
        }
        else if (input.value.length > 18) {
            inputNumberValue = getInputOnlyNumber(input);
            input.value = addMask(inputNumberValue);
            // Ставим курсор в нужную  позицию
            if (input.value[cursorPointer-1] == ")") {
                input.selectionStart = cursorPointer + 2;
            }
           else if (input.value[cursorPointer-1] == "(" || input.value[cursorPointer-1] == "-") {
                input.selectionStart = cursorPointer + 1;
            }
            else {
                input.selectionStart = cursorPointer;
            }
        }
        return;
    }
    if (["3", "8", "0", "9"].indexOf(inputNumberValue[0]) > -1 || ["+"].indexOf(inputValue[0]) > -1){
        // Если номер украинский
        inputNumberValue = checkFirstDigit(inputNumberValue);
        
        // Добавляем маску
        formatedValue = addMask(inputNumberValue);
        return input.value = formatedValue;
    }
    else {
        // Not Ukrainian number
        return input.value = "+" + inputNumberValue.substring(0, 12);
    }

}
var phonePasted = (e) =>  {
    // Обработка события вставки через Ctrl + V
    let pasted_obj = e.clipboardData || window.clipboardData,
        input = e.target,
        inputNumberValue = getInputOnlyNumber(input);
    
    if (pasted_obj) {
        let pastedText = pasted_obj.getData("Text");
        if (/\D/g.test(pastedText)) {
            input.value = inputNumberValue;
        }
    }
}

var phone_mask = (phone_selector) => {
    // главная функция котораю будет прикручиватся к input
    var phone_inputs = document.querySelectorAll(phone_selector);
    phone_inputs.forEach((phone) => {
        phone.type = "tel";
        phone.addEventListener('input', phoneInput);
        phone.addEventListener('paste', phonePasted);
    });
}

function menuToggle(){
    let menuBtn=document.getElementById('menuBtn');
    let header=document.getElementById('myHeader');
    header.classList.toggle('menuActive');
    menuBtn.classList.toggle('isActive');
}
function contactToggle(){
    let form=document.getElementById('contactWrap')
    form.classList.toggle('isActive')
}
$(".scroll_link").click(function() {
    var element_id = $(this).attr("data-element");
    $([document.documentElement, document.body]).animate({
        scrollTop: $(element_id).offset().top
    }, 400);
    $("#myHeader").removeClass("menuActive");
    $("#menuBtn").removeClass("isActive");
});
$(".js-order-form").click(function() {
    $(".modal").addClass("open");
});
$(".js-close-modal").click(function() {
    $(".modal").removeClass("open");
});
AOS.init();

jQuery('.js-clean-slider').slick({
    dots: false,
    autoplay: true,
    autoplaySpeed: 2000,
    speed: 300,
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: true,
});
jQuery(".js-reviews-slider").slick({
    dots: true,
    autoplay: false,
    // autoplaySpeed: 3000,
    speed: 300,
    slidesToShow: 4,
    slidesToScroll: 1,
    arrows: true,
    responsive: [
        {
          breakpoint: 1024,
          settings: {
            slidesToShow: 3,
            slidesToScroll: 3,
            infinite: true,
            dots: true
          }
        },
        {
          breakpoint: 860,
          settings: {
            slidesToShow: 2,
            slidesToScroll: 2
          }
        },
        {
          breakpoint: 560,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1
          }
        }
      ]
});
jQuery(".js-product-slider").slick({
    dots: true,
    autoplay: true,
    autoplaySpeed: 3000,
    speed: 300,
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: false,
});

$(document).ready(function() {
    console.log(document.cookie);
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
    const csrftoken = getCookie('csrftoken');
    $("body").on("click", ".js-add-to-cart", function() {
        console.log("Click add to cart");
        console.log(csrftoken);
        let url = $(this).attr("data-url");
        let product_id = $(this).attr("data-id");
        $.ajax({
            url: url,
            type: "POST",
            headers: {'X-CSRFToken': csrftoken},
            data: {
                "csrfmiddlewaretoken": csrftoken,
                "product_id": product_id,
            },
            success: function(responce) {
                $(".js-modal-content").html(responce.html);
                $(".js-cart-quantity").text(responce.quantity);
                $(".js-modal").addClass("open");
                phone_mask(".js-phone-mask");
            },
        });
    });
    $("body").on("click", ".js-show-cart", function() {
        let url = $(this).attr("data-url");
        let is_cleaning = $(this).attr("data-cleaning");
        let is_change_battery = $(this).attr("data-battery");
        $.ajax({
            url: url,
            type: "GET",
            headers: {'X-CSRFToken': csrftoken},
            data: {
                "is_cleaning": is_cleaning,
                "is_change_battery": is_change_battery,
            },
            success: function(responce) {
                $(".js-modal-content").html(responce.html);
                $(".js-cart-quantity").text(responce.quantity);
                $(".js-modal").addClass("open");
                phone_mask(".js-phone-mask");
            },
        });
    });
    $("body").on("click", ".js-delete-from-cart", function() {
        let url = $(this).attr("data-url");
        let item_id = $(this).attr("data-id");
        $.ajax({
            url: url,
            type: "POST",
            headers: {'X-CSRFToken': csrftoken},
            data: {
                "csrfmiddlewaretoken": getCookie('csrftoken'),
                "item_id": item_id,
            },
            success: function(responce) {
                $(".js-modal-content").html(responce.html);
                $(".js-cart-quantity").text(responce.quantity);
                $(".js-modal").addClass("open");
                phone_mask(".js-phone-mask");
            },
        });
    });
    $("body").on("submit", ".js-order-form", function(e) {
        e.preventDefault();
        console.log("Send")
        let url = $(this).attr("action");
        $.ajax({
            url: $(this).attr("action"),
            type: "POST",
            headers: {'X-CSRFToken': csrftoken},
            data: $(this).serialize(),
            success: function(responce) {
                console.log("Recive")
                $(".js-modal-content").html(responce.html);
            }
        })
    });
    $("body").on("click", ".js-gallery-img",  function (){
        let info_bock = $(this).children(".info");
        info_bock.toggleClass("show")
    })
})