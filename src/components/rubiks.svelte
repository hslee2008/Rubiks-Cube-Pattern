<script>
  import { onMount } from 'svelte'

  export let cubeMethod = {
    execute: moves => {},
    reset: () => {}
  }

  export let cubeType = 1
  export let speed
  let myCube

  onMount(() => {
    import('jquery').then($ => {
      const $$ = $.default

      import('./jquery.cube.threejs.min.js').then(() => {
        $$(function () {
          cubeMethod.execute = moves => {
            myCube = $$('.cube').cube({
              background: 0xf0f0f0,
              type: cubeType,
              animation: {
                delay: speed
              }
            })

            myCube.execute(moves)
          }
          cubeMethod.reset = () => {
            myCube.reset()
          }
        })
      })
    })
  })

  function zoomIn() {
    myCube.zoomIn()
  }

  function zoomOut() {
    myCube.zoomOut()
  }
</script>

<div>
  <div class="toolbar">
    <button class="toolbar-btn" on:click="{zoomIn}">+</button>
    <button class="toolbar-btn" on:click="{zoomOut}">-</button>
  </div>
  <div class="cube"></div>
</div>

<style>
  .cube {
    width: 400px;
    height: 400px;
    margin-left: auto;
    margin-right: auto;
    margin-top: 20px;
    overflow: auto;
  }

  @media (max-width: 768px) {
    .cube {
      width: 300px;
      height: 300px;
    }
  }
</style>
