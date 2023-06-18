'use strict'

const CACHE_NAME = 'finals-calculator-v8'

const FILES_TO_CACHE = [
  '/images/48x48.png',
  '/images/72x72.png',
  '/images/96x96.png',
  '/images/144x144.png',
  '/images/512x512.png',
  '/images/maskable_icon.png',
  '/icon.png',
  '/manifest.json'
]

self.addEventListener('install', evt => {
  evt.waitUntil(
    caches.open(CACHE_NAME).then(cache => cache.addAll(FILES_TO_CACHE))
  )
  self.skipWaiting()
})

self.addEventListener('activate', evt => {
  // Remove previous cached data from disk.
  evt.waitUntil(
    caches.keys().then(keyList => {
      return Promise.all(
        keyList.map(key => {
          if (key !== CACHE_NAME) {
            return caches.delete(key)
          }
        })
      )
    })
  )

  self.clients.claim()
})

self.addEventListener('fetch', evt => {
  if (evt.request.mode !== 'navigate') return

  evt.respondWith(
    fetch(evt.request).catch(async () => {
      const cache = await caches.open(CACHE_NAME)
      return await cache.match('offline.html')
    })
  )
})
