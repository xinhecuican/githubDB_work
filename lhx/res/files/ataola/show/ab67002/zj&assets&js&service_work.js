if (navigator.serviceWorker) {
  navigator.serviceWorker
    .register('./assets/js/sw.js')
    .then(function(registration) {
      console.log(`${registration} service worker 注册成功`);
    })
    .catch(function(err) {
      console.log(`${err} service worker 注册失败`);
    })
}