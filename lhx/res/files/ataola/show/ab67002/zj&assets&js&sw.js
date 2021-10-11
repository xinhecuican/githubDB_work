self.addEventListener('install', e => {
  e.waitUntil(
    caches.open('my-cache').then(function(cache){
      return cache.addAll(['../../service-worker.html', './service_work.js']);
    })
  )
})

self.addEventListener('fetch', e => {
  e.respondWith(
    caches.match(e.request).then(function(response) {
      if (response) {
        return response;
      }
      console.log('fetch source');
    })
  )
})