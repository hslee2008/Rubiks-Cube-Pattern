<script>
  import {
    TextInput,
    Modal,
    ModalBody,
    DataTable,
    Slider
  } from 'carbon-components-svelte'
  import Cube from 'rubiks-cube'
  import Rubiks from '../components/rubiks.svelte'

  let pattern = 'R R U U'
  let completeMove = ''
  let moveCount = 0
  let cubeType = 3
  let speed = 1000
  let openedCalc = false
  let cubeMethod

  let headers = [
    {
      key: 'move',
      value: 'Move'
    },
    {
      key: 'count',
      value: 'Count'
    }
  ]
  let rows = []

  $: rows = [
    {
      id: 'move',
      move: pattern,
      count: moveCount
    }
  ]

  function calculateMovesToFinishPattern(pattern) {
    const cube = new Cube()
    const patternCube = Cube.scramble(pattern)

    completeMove = `${pattern} `

    let moveCount = 1
    while (!patternCube.isSolved()) {
      patternCube.scramble(pattern)
      completeMove += `${pattern} `
      moveCount++
    }

    completeMove = completeMove.trim()

    return moveCount
  }

  function calculate() {
    openedCalc = true
    moveCount = calculateMovesToFinishPattern(pattern)
    setTimeout(() => cubeMethod.execute(completeMove), 100)
  }
</script>

<div class="mb20">
  <h1>반복 횟수 계산기</h1>
</div>

<div class="mb20">
  <TextInput bind:value="{pattern}" labelText="패턴" />
</div>

<div class="mb20">
  <TextInput bind:value="{cubeType}" labelText="큐브 종류" />
</div>

<Slider
  labelText="스피드"
  hideTextInput
  bind:value="{speed}"
  fullWidth
  min="{1}"
  max="{1000}"
/>

{#if openedCalc}
<Modal
  bind:open="{openedCalc}"
  size="lg"
  modalHeading="반복 횟수 계산기"
  passiveModal
  selectorPrimaryFocus=".bx--modal-content"
  on:close="{() => cubeMethod.reset()}"
>
  <DataTable bind:headers bind:rows />
  <Rubiks bind:cubeMethod bind:cubeType bind:speed></Rubiks>
</Modal>
{/if}

<button class="main-btn" on:click="{calculate}">계산하기</button>
