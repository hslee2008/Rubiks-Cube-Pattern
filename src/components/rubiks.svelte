<script>
  import { onMount } from 'svelte'

  export let cubeMethod = {
    execute: moves => {},
    reset: () => {}
  }

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
              type: 3,
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
</script>

<div class="cube"></div>

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
