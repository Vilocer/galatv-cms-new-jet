$(function () {
    // WOW effect
    $('.wow-effect').each(function(i, element) {
        $(element).addClass('wow-effect__active');
    });

    // Toolbar with header
    if ( $('.cms-toolbar').length > 0 ){
        $('.header').addClass('header--with--toolbar');

    } // Класс header--with-toolbar делает header сверху с отступом в 45px, для того чтобы он не закрывался toolbar'ом
    // Fixed Header
    var page_id = $('.page').attr('id'),
        header = $('#header'),
        headerH = header.innerHeight(),
        scrollOffset =  $(window).scrollTop();
        
    checkScroll(scrollOffset); // При загруке страници сразу вне header

    $(window).on('scroll', function() {

        scrollOffset = $(this).scrollTop();
        checkScroll(scrollOffset);

    });

    function checkScroll(scrollOffset) {

        if ( scrollOffset >= headerH || page_id != 'page--home')  { 
            header.addClass('active');

        } else {
            header.removeClass('active');

        }
    }

    // Nav Toggle
    $('#nav__toggle').on("click", function(e) {
        e.preventDefault();

        $("#nav__toggle").toggleClass('active');
        $("#nav__menu").toggleClass('active');

    });

    // Smooth Scroll
    $('[data-scroll]').on('click', function(e) {

        // Get offset for scroll
        var $this = $(this),
            blockId = $this.data('scroll'),
            blockOffset = $(blockId).offset().top - 80;

        e.preventDefault()
        
        // Set current link active
        $('#nav .nav__link').removeClass('active');
        $this.addClass('active');

        // Set current link active in menu
        $('#nav__menu .nav__menu__link').removeClass('active');
        $('#nav__menu .nav__menu__link[data-scroll="' + blockId + '"]').addClass('active');

        // Да, у нас есть функция setActiveLinks, которая работает по скроллу, но она работает только после скролла.
        // Т.е. с задержкой, это её предотвращает.

        // Scroll to Element
        $('html, body').animate({
            scrollTop: blockOffset
        }, 500);

        // Close nav for mobile
        $('#nav__menu').removeClass('active');
        $('#nav__toggle').removeClass('active');

    });

    // Auto Active Nav Link on just scroll
    const sectionsHeights = new Map();

    $("#main").children().each( function( i, section ) {
        var sectionId = section.id,
            sectionH = $(section).offset().top; // Узнаеём позиция секции, считая сверху

        sectionsHeights.set(sectionId, sectionH); // Записываем в словарь

    });

    $(window).on('scroll', function() {
        var scrollOffset = $(this).scrollTop();

        setActiveLinks(scrollOffset);

    });

    function setActiveLinks( scrollOffset ) {

        var currentSection; // В неё будет записываться последняя пролистанная секция, т.е. та, для которой scrollOffset больше её позиции

        for ( var section of sectionsHeights ){
            if ( scrollOffset >= section[1] - 150 ) { // id[0] - section id, id[1] - section height
                currentSection = section;
            }
            else {
                break

            }

        }

        //  Clear all active links
        $(`.nav__link`).removeClass('active');
        $(`.nav__menu__link`).removeClass('active');

        if (currentSection) {
            $(`.nav__link[data-scroll="#${ currentSection[0] }"]`).addClass('active'); // set link active on nav
            $(`.nav__menu__link[data-scroll="#${ currentSection[0] }"]`).addClass('active');; // set link active on nav menu
        }

    }

    // Header Search
    $('#search__link').click( function(e) {
        if (($('#search__input').val() == '')) {
            e.preventDefault();

        }

    });

    // Modals
    $('.modal__link').each( function(e, modalLink) {

        var modalLink = $(modalLink),
            dataModal = modalLink.data('modal'),
            modal = $(`#${ dataModal }`),
            modalContent = $(`#${ dataModal } .modal__content`),
            modalClose = $(`#${ dataModal } .modal__close`);

        modalLink.on('click', function(e) { 
            e.preventDefault();
            modal.addClass('active'); // Make modal active on link click

        });

        modalClose.on('click', function(e) { 
            e.preventDefault();
            modal.removeClass('active');// Make modal deactive on link close

        });

        // Close Modal on click outside a modal content and outside a link
        $(window).on('click', function(e) {
            if (!modalContent.is(e.target)
                && modalContent.has(e.target).length === 0
                && !modalLink.is(e.target)
                && modalLink.has(e.target).length === 0 ) {
                modal.removeClass('active');

            }

        });

    });

    // Rates Price
    $('.rates__switch input').on("click", function(e){
        var $this = $(this),
            priceDiv = $(`.rates__item[data-name="${ $this.data("up-price-to") }"] .price`);

        // For Rate in Modals
        if (priceDiv.length == 0) {
            priceDiv = $(`.rates__modal__item[data-name="${ $this.data("up-price-to") }"] .price`);
        }

        var price = Number(priceDiv.text());

        if (this.checked) { // Up Pice by data-up-price-by, on click switch on
            var totalPrice = price + Number($this.data("up-price-by"));
            priceDiv.text(totalPrice);

        }
        else { // Down Pice by data-up-price-by, on click switch off
            var totalPrice = price - Number($this.data("up-price-by"));
            priceDiv.text(totalPrice);
        }

    });

});