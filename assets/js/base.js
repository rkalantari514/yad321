if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('service-worker.js').then(_0x31fe41 => console.log('service worker registered')).catch(_0x291344 => console.log('service worker not registered - there is an error.', _0x291344));
}
$(document).ready(function () {
  setTimeout(() => {
      if ('kyFps' === 'kyFps') {
          $('#loader').fadeToggle(250);
      } else {
          $('.goTop.button').removeClass('show');
      }
  }, 700);
});
$('a[href="#"]').click(function (_0x3f0bb0) {
  _0x3f0bb0.preventDefault();
});
$('.goTop').click(function (_0x3c4a8b) {
  _0x3c4a8b.preventDefault();
  $('html, body').animate({
      'scrollTop': 0x0
  }, 'slow');
});
function goDownButton() {
  var _0x4ef8fc = $(this).scrollTop();
  if (_0x4ef8fc > 350) {
      if ('cyrDS' === 'cyrDS') {
          $('.goTop.button').addClass('show');
      } else {
          time = time + 300;
          setTimeout(() => {
              $('.notification-box').removeClass('show');
          }, time);
      }
  } else {
      if ('dFHah' === 'dFHah') {
          $('.goTop.button').removeClass('show');
      } else {
          $('#android-add-to-home-screen').modal();
      }
  }
}
goDownButton();
$(window).scroll(function () {
  goDownButton();
});
$('.goBack').click(function () {
  window.history.go(-1);
});
$('.adbox .closebutton').click(function () {
  $(this).parent('.adbox').addClass('hide');
});
var osDetection = navigator.userAgent || navigator.vendor || window.opera;
var windowsPhoneDetection = /windows phone/i.test(osDetection);
var androidDetection = /android/i.test(osDetection);
var iosDetection = /iPad|iPhone|iPod/ ['test'](osDetection) && !window.MSStream;
if (windowsPhoneDetection) {
  $('.windowsphone-detection').addClass('is-active');
  $('.mobile-detection').addClass('is-active');
} else if (androidDetection) {
  $('.android-detection').addClass('is-active');
  $('.mobile-detection').addClass('is-active');
} else if (iosDetection) {
  $('.ios-detection').addClass('is-active');
  $('.mobile-detection').addClass('is-active');
} else {
  $('.non-mobile-detection').addClass('is-active');
}
$(function () {
  $('[data-toggle="tooltip"]').tooltip();
});
$('.clear-input').click(function () {
  $(this).parent('.input-wrapper').find('.form-control').focus();
  $(this).parent('.input-wrapper').find('.form-control').val('');
  $(this).parent('.input-wrapper').removeClass('not-empty');
});
$('.form-group .form-control').focus(function () {
  $(this).parent('.input-wrapper').addClass('active');
}).blur(function () {
  $(this).parent('.input-wrapper').removeClass('active');
});
$('.form-group .form-control').keyup(function () {
  var _0x4f674b = $(this).val().length;
  if (_0x4f674b > 0) {
      if ('kQwas' !== 'QygPs') {
          $(this).parent('.input-wrapper').addClass('not-empty');
      } else {
          var _0x340e24 = $(this).val().length;
          if (_0x340e24 > 0) {
              $(this).parent('.input-wrapper').addClass('not-empty');
          } else {
              $(this).parent('.input-wrapper').removeClass('not-empty');
          }
      }
  } else {
      $(this).parent('.input-wrapper').removeClass('not-empty');
  }
});
$('.toggle-searchbox').click(function () {
  var _0xddd392 = $('#search').hasClass('show');
  if (_0xddd392) {
      if ('JDrEB' !== 'JDrEB') {
          $(this).next('ul').slideToggle(250);
          $(this).parent('.multi-level').removeClass('active');
      } else {
          $('#search').removeClass('show');
      }
  } else {
      if ('zLzsy' === 'hJCQs') {
          $('#search').removeClass('show');
      } else {
          $('#search').addClass('show');
          $('#search .form-control').focus();
      }
  }
});
$('body').on('click', '.stepper-up', function () {
  var _0x37ec18 = $(this).parent('.stepper').children('.form-control');
  _0x37ec18.val(parseInt(_0x37ec18.val()) + 1);
});
$('body').on('click', '.stepper-down', function () {
  var _0x250a29 = $(this).parent('.stepper').children('.form-control');
  if (parseInt(_0x250a29.val()) < 1) {} else {
      if ('KmGPZ' !== 'HMPUN') {
          _0x250a29.val(parseInt(_0x250a29.val()) - 1);
      } else {
          $('.windowsphone-detection').addClass('is-active');
          $('.mobile-detection').addClass('is-active');
      }
  }
});
$('.carousel-full').owlCarousel({
    'rtl':true ,
  'loop': true,
  'margin': 0,
  'nav': false,
  'items': 1,
  'dots': false
});
$('.carousel-single').owlCarousel({
    'rtl':true ,
  'stagePadding': 30,
  'loop': true,
  'margin': 16,
  'nav': false,
  'dots': false,
  'responsiveClass': true,
  'responsive': {
      0: {
          'items': 0x1
      },
      768: {
          'items': 0x3
      }
  }
});
$('.carousel-multiple').owlCarousel({
    'rtl':true ,
  'stagePadding': 32,
  'loop': true,
  'margin': 16,
  'nav': false,
  'items': 2,
  'dots': false,
  'responsiveClass': true,
  'responsive': {
      0: {
          'items': 0x2
      },
      768: {
          'items': 0x4
      }
  }
});
$('.carousel-small').owlCarousel({
    'rtl':true ,
  'stagePadding': 32,
  'loop': true,
  'margin': 16,
  'nav': false,
  'items': 5,
  'dots': false,
  'responsiveClass': true,
  'responsive': {
      0: {
          'items': 0x5
      },
      768: {
          'items': 0x8
      }
  }
});
$('.carousel-slider').owlCarousel({
    'rtl':true ,
  'loop': true,
  'margin': 8,
  'nav': false,
  'items': 1,
  'dots': true
});
function notification(_0x3a3df7, _0x5e4771) {
  var _0x301962 = '#' + _0x3a3df7;
  $('.notification-box').removeClass('show');
  setTimeout(() => {
      if ('tZDsL' !== 'tZDsL') {
          $('.dark-mode-switch').attr('checked', true);
          if ($('body').hasClass('dark-mode-active')) {} else {
              $('body').addClass('dark-mode-active');
          }
      } else {
          $(_0x301962).addClass('show');
      }
  }, 300);
  if (_0x5e4771) {
      _0x5e4771 = _0x5e4771 + 300;
      setTimeout(() => {
          if ('kTaUz' === 'kTaUz') {
              $('.notification-box').removeClass('show');
          } else {
              event.preventDefault();
              $('html, body').animate({
                  'scrollTop': 0x0
              }, 'slow');
          }
      }, _0x5e4771);
  }
};
$('.notification-box .close-button').click(function (_0x53ad40) {
  _0x53ad40.preventDefault();
  $('.notification-box.show').removeClass('show');
});
$('.notification-box.tap-to-close .notification-dialog').click(function () {
  $('.notification-box.show').removeClass('show');
});
function toastbox(_0x15d277, _0x5c0770) {
  var _0x42f830 = '#' + _0x15d277;
  $('.toast-box').removeClass('show');
  setTimeout(() => {
      $(_0x42f830).addClass('show');
  }, 100);
  if (_0x5c0770) {
      if ('wFLcY' !== 'wFLcY') {
          $(this).removeClass('show');
      } else {
          _0x5c0770 = _0x5c0770 + 100;
          setTimeout(() => {
              if ('ZkFXf' === 'ZkFXf') {
                  $('.toast-box').removeClass('show');
              } else {
                  dmswitch.prop('checked', this.checked);
              }
          }, _0x5c0770);
      }
  }
};
$('.toast-box .close-button').click(function (_0x333d97) {
  _0x333d97.preventDefault();
  $('.toast-box.show').removeClass('show');
});
$('.toast-box.tap-to-close').click(function () {
  $(this).removeClass('show');
});
function animatedHeader() {
  var _0x2929d1 = $(this).scrollTop();
  if (_0x2929d1 > 20) {
      $('.appHeader.scrolled').addClass('is-active');
  } else {
      if ('Qfenq' !== 'SSQxh') {
          $('.appHeader.scrolled').removeClass('is-active');
      } else {
          $('#online-toast').removeClass('show');
      }
  }
}
animatedHeader();
$(window).scroll(function () {
  animatedHeader();
});
var OnlineText = 'به اینترنت متصل هستید';
var OfflineText = 'متاسفانه اینترنت شما وصل نیست';
function onlineModeToast() {
  $('body').append("<div id='online-toast' class='toast-box bg-success toast-top tap-to-close'>" + "<div class='in'><div class='text'>" + OnlineText + '</div></div></div>');
  setTimeout(() => {
      if ('uiZHc' === 'uiZHc') {
          toastbox('online-toast', 3000);
      } else {
          $('.notification-box.show').removeClass('show');
      }
  }, 500);
}
function offlineModeToast() {
  $('body').append("<div id='offline-toast' class='toast-box bg-danger toast-top tap-to-close'>" + "<div class='in'><div class='text'>" + OfflineText + '</div></div></div>');
  setTimeout(() => {
      if ('EfJZa' !== 'GEKMO') {
          toastbox('offline-toast');
      } else {
          if ($('body').hasClass('dark-mode-active')) {
              $('body').removeClass('dark-mode-active');
          }
          localStorage.setItem('MobilekitDarkModeActive', '0');
          $('.dark-mode-switch').attr('checked', false);
      }
  }, 500);
}
function onlineMode() {
  if ($('#offline-toast').hasClass('show')) {
      if ('Ljghw' !== 'Ljghw') {
          $('body').addClass('dark-mode-active');
      } else {
          $('#offline-toast').removeClass('show');
      }
  }
  if ($('#online-toast').length > 0) {
      if ('IrDeV' !== 'IrDeV') {
          $(this).parent('.multi-level').parent('ul').children('li').children('ul').slideUp(250);
          $(this).next('ul').slideToggle(250);
          $(this).parent('.multi-level').parent('ul').children('.multi-level').removeClass('active');
          $(this).parent('.multi-level').addClass('active');
      } else {
          $('#online-toast').addClass('show');
          setTimeout(() => {
              if ('gIOoB' === 'gIOoB') {
                  $('#online-toast').removeClass('show');
              } else {
                  $('[data-toggle=\"tooltip\"]').tooltip();
              }
          }, 3000);
      }
  } else {
      if ('wSROb' !== 'bxWIQ') {
          onlineModeToast();
      } else {
          var _0x33bab1 = '#' + target;
          $('.toast-box').removeClass('show');
          setTimeout(() => {
              $(_0x33bab1).addClass('show');
          }, 100);
          if (time) {
              time = time + 100;
              setTimeout(() => {
                  $('.toast-box').removeClass('show');
              }, time);
          }
      }
  }
  $('.toast-box.tap-to-close').click(function () {
      if ('UdoxH' === 'lBPyr') {
          event.preventDefault();
          $('.notification-box.show').removeClass('show');
      } else {
          $(this).removeClass('show');
      }
  });
}
function offlineMode() {
  if ($('#online-toast').hasClass('show')) {
      if ('YDFsE' === 'tUCkz') {
          $('.dark-mode-switch').trigger('.dark-mode-switch');
          var _0x520dd0 = localStorage.getItem('MobilekitDarkModeActive');
          if (_0x520dd0 === 1 || _0x520dd0 === '1') {
              if ($('body').hasClass('dark-mode-active')) {
                  $('body').removeClass('dark-mode-active');
              }
              localStorage.setItem('MobilekitDarkModeActive', '0');
              $('.dark-mode-switch').attr('checked', false);
          } else {
              $('body').addClass('dark-mode-active');
              $('.dark-mode-switch').attr('checked', true);
              localStorage.setItem('MobilekitDarkModeActive', '1');
          }
      } else {
          $('#online-toast').removeClass('show');
      }
  }
  if ($('#offline-toast').length > 0) {
      if ('dPCjG' === 'zeoAz') {
          event.preventDefault();
          $('.toast-box.show').removeClass('show');
      } else {
          $('#offline-toast').addClass('show');
      }
  } else {
      if ('nZTZl' !== 'lqYye') {
          offlineModeToast();
      } else {
          $('body').addClass('dark-mode-active');
          $('.dark-mode-switch').attr('checked', true);
          localStorage.setItem('MobilekitDarkModeActive', '1');
      }
  }
  $('.toast-box.tap-to-close').click(function () {
      if ('pkFWy' !== 'Awwdc') {
          $(this).removeClass('show');
      } else {
          animatedHeader();
      }
  });
}
window.addEventListener('online', onlineMode);
window.addEventListener('offline', offlineMode);
$('.custom-file-upload input[type="file"]').each(function () {
  var _0x471b57 = $(this),
      _0x5ad3d0 = _0x471b57.next('label'),
      _0x5a2d45 = _0x5ad3d0.find('span'),
      _0x357a8c = _0x5a2d45.text();
  _0x471b57.on('change', function (_0xbee35f) {
      if ('ibCEX' !== 'ibCEX') {
          _0x5ad3d0.removeClass('file-uploaded');
          _0x5a2d45.text(_0x357a8c);
      } else {
          var _0xd6f8bc = _0x471b57.val().split('\\').pop(),
              _0x386daf = URL.createObjectURL(_0xbee35f.target.files[0]);
          if (_0xd6f8bc) {
              if ('FAucN' !== 'FAucN') {
                  $('.goTop.button').addClass('show');
              } else {
                  _0x5ad3d0.addClass('file-uploaded').css('background-image', 'url(' + _0x386daf + ')');
                  _0x5a2d45.text(_0xd6f8bc);
              }
          } else {
              _0x5ad3d0.removeClass('file-uploaded');
              _0x5a2d45.text(_0x357a8c);
          }
      }
  });
});
$('.multi-level > a.item').click(function () {
  if ($(this).parent('.multi-level').hasClass('active')) {
      if ('QRnLU' === 'LYbme') {
          var _0x1c9049 = $(this),
              _0x3f0382 = _0x1c9049.next('label'),
              _0x5e953a = _0x3f0382.find('span'),
              _0x130182 = _0x5e953a.text();
          _0x1c9049.on('change', function (_0x2a860d) {
              var _0x127b3c = _0x1c9049.val().split('\\').pop(),
                  _0x3b3d3e = URL.createObjectURL(_0x2a860d.target.files[0]);
              if (_0x127b3c) {
                  _0x3f0382.addClass('file-uploaded').css('background-image', 'url(' + _0x3b3d3e + ')');
                  _0x5e953a.text(_0x127b3c);
              } else {
                  _0x3f0382.removeClass('file-uploaded');
                  _0x5e953a.text(_0x130182);
              }
          });
      } else {
          $(this).next('ul').slideToggle(250);
          $(this).parent('.multi-level').removeClass('active');
      }
  } else {
      if ('tKTjo' === 'tKTjo') {
          $(this).parent('.multi-level').parent('ul').children('li').children('ul').slideUp(250);
          $(this).next('ul').slideToggle(250);
          $(this).parent('.multi-level').parent('ul').children('.multi-level').removeClass('active');
          $(this).parent('.multi-level').addClass('active');
      } else {
          var _0x3b3f4a = '#' + target;
          $('.notification-box').removeClass('show');
          setTimeout(() => {
              $(_0x3b3f4a).addClass('show');
          }, 300);
          if (time) {
              time = time + 300;
              setTimeout(() => {
                  $('.notification-box').removeClass('show');
              }, time);
          }
      }
  }
});
function AddtoHome(_0x5011e6, _0x3a84f1) {
  if (_0x3a84f1) {
      var _0x4f8716 = localStorage.getItem('MobilekitAddHomeStatus');
      if (_0x4f8716 === '1' || _0x4f8716 === 1) {} else {
          localStorage.setItem('MobilekitAddHomeStatus', 1);
          window.addEventListener('load', () => {
              if ('NzeOt' === 'NzeOt') {
                  if (navigator.standalone) {} else if (matchMedia('(display-mode: standalone)').matches) {} else {
                      if ('NclqM' === 'DIHXL') {
                          toastbox('online-toast', 3000);
                      } else {
                          if (androidDetection) {
                              if ('NyfgH' === 'NyfgH') {
                                  setTimeout(() => {
                                      $('#android-add-to-home-screen').modal();
                                  }, _0x5011e6);
                              } else {
                                  setTimeout(() => {
                                      $('#android-add-to-home-screen').modal();
                                  }, _0x5011e6);
                              }
                          }
                          if (iosDetection) {
                              if ('Kxxjq' !== 'Kxxjq') {
                                  $('#offline-toast').addClass('show');
                              } else {
                                  setTimeout(() => {
                                      if ('gQmnS' !== 'gQmnS') {
                                          var _0x56765b = $('#search').hasClass('show');
                                          if (_0x56765b) {
                                              $('#search').removeClass('show');
                                          } else {
                                              $('#search').addClass('show');
                                              $('#search .form-control').focus();
                                          }
                                      } else {
                                          $('#ios-add-to-home-screen').modal();
                                      }
                                  }, _0x5011e6);
                              }
                          }
                      }
                  }
              } else {
                  $('body').append("<div id='online-toast' class='toast-box bg-success toast-top tap-to-close'>" + "<div class='in'><div class='text'>" + OnlineText + '</div></div></div>');
                  setTimeout(() => {
                      toastbox('online-toast', 3000);
                  }, 500);
              }
          });
      }
  } else {
      if ('nvxNr' !== 'GJEEA') {
          window.addEventListener('load', () => {
              if ('hotJd' !== 'LPmXm') {
                  if (navigator.standalone) {} else if (matchMedia('(display-mode: standalone)').matches) {} else {
                      if ('jjuzr' !== 'jjuzr') {
                          var _0x49e338 = $(this).scrollTop();
                          if (_0x49e338 > 20) {
                              $('.appHeader.scrolled').addClass('is-active');
                          } else {
                              $('.appHeader.scrolled').removeClass('is-active');
                          }
                      } else {
                          if (androidDetection) {
                              if ('bUGFx' !== 'MLWWE') {
                                  setTimeout(() => {
                                      if ('rNWhX' === 'rNWhX') {
                                          $('#android-add-to-home-screen').modal();
                                      } else {
                                          $('.non-mobile-detection').addClass('is-active');
                                      }
                                  }, _0x5011e6);
                              } else {
                                  _0x5011e6 = _0x5011e6 + 100;
                                  setTimeout(() => {
                                      $('.toast-box').removeClass('show');
                                  }, _0x5011e6);
                              }
                          }
                          if (iosDetection) {
                              if ('ZhcvT' !== 'ZhcvT') {
                                  e.preventDefault();
                              } else {
                                  setTimeout(() => {
                                      if ('fDKTW' === 'fDKTW') {
                                          $('#ios-add-to-home-screen').modal();
                                      } else {
                                          $('.appHeader.scrolled').removeClass('is-active');
                                      }
                                  }, _0x5011e6);
                              }
                          }
                      }
                  }
              } else {
                  navigator.serviceWorker.register('service-worker.js').then(_0x4ec322 => console.log('service worker registered')).catch(_0x312b48 => console.log('service worker not registered - there is an error.', _0x312b48));
              }
          });
      } else {
          $(a).addClass('show');
      }
  }
}
var checkDarkModeStatus = localStorage.getItem('MobilekitDarkModeActive');
if (checkDarkModeStatus === 1 || checkDarkModeStatus === '1') {
  $('.dark-mode-switch').attr('checked', true);
  if ($('body').hasClass('dark-mode-active')) {} else {
      $('body').addClass('dark-mode-active');
  }
} else {
  $('.dark-mode-switch').attr('checked', false);
}
$('.dark-mode-switch').change(function () {
  $('.dark-mode-switch').trigger('.dark-mode-switch');
  var _0x36876f = localStorage.getItem('MobilekitDarkModeActive');
  if (_0x36876f === 1 || _0x36876f === '1') {
      if ('nPvyJ' !== 'nPvyJ') {
          $('#android-add-to-home-screen').modal();
      } else {
          if ($('body').hasClass('dark-mode-active')) {
              if ('WXzDQ' !== 'lDMDR') {
                  $('body').removeClass('dark-mode-active');
              } else {
                  $('body').removeClass('dark-mode-active');
              }
          }
          localStorage.setItem('MobilekitDarkModeActive', '0');
          $('.dark-mode-switch').attr('checked', false);
      }
  } else {
      if ('OGaBi' === 'OGaBi') {
          $('body').addClass('dark-mode-active');
          $('.dark-mode-switch').attr('checked', true);
          localStorage.setItem('MobilekitDarkModeActive', '1');
      } else {
          setTimeout(() => {
              $('#ios-add-to-home-screen').modal();
          }, time);
      }
  }
});
var dmswitch = $('.dark-mode-switch');
dmswitch.on('change', function () {
  dmswitch.prop('checked', this.checked);
});


// ===============

if ($('body').hasClass('dark-mode-active')) {
    var element = document.getElementsByClassName('why')
    // $('why').addClass('dark')
    element.classList.add("dark");
} else{
    // $('why').addClass('light')
    element.classList.add("light");
}

function whytoggle() {
    var element = document.getElementsByClassName('why')
    element.classList.add("mystyle");
    element.classList.add("dark");
 }