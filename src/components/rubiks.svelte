<script>
  import { onMount } from 'svelte'

  export const cubeMethod = {
    execute: moves => {},
    reset: () => {}
  }

  export let cubeType = 1
  export let speed

  onMount(() => {
    import('jquery').then($ => {
      const $$ = $.default

      import('./jquery.cube.threejs.min.js').then(() => {
        $$(function () {
          let myCube

          cubeMethod.execute = moves => {
            myCube = $$('.cube').cube({
              color: [
                0xff0000, 0xff8000, 0xffff00, 0x555555, 0x0000ff, 0x00ff00,
                0xffffff
              ],
              background: 0xf0f0f0,
              type: cubeType,
              animation: {
                duration: speed,
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
  }

  @media (max-width: 768px) {
    .cube {
      width: 300px;
      height: 300px;
    }
  }
</style>
