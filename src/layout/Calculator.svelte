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
  import humanizeDuration from 'humanize-duration'

  let pattern = 'R R U U'
  let completeMove = ''
  let moveCount = 0
  let speed = 1000
  let openedCalc = false
  let cubeMethod = {}

  let headers = [
    {
      key: 'category',
      value: 'Category'
    },
    {
      key: 'value',
      value: 'Explanation'
    }
  ]
  let rows = []

  $: rows = [
    {
      id: 'move',
      category: '패턴',
      value: pattern
    },
    {
      id: 'turns',
      category: '반복 횟수',
      value: moveCount
    },
    {
      id: 'totalTurns',
      category: '총 돌림 횟수',
      value: moveCount * ((pattern.length - 1) / 2 + 1)
    },
    {
      id: 'time',
      category: '예상 시간',
      value: humanizeDuration(
        Math.ceil(moveCount * ((pattern.length - 1) / 2 + 1) * speed)
      )
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
    setTimeout(() => cubeMethod.execute(completeMove), 200)
  }
</script>

<div class="mb20">
  <h1>반복 횟수 계산기</h1>
</div>

<div class="mb20">
  <TextInput bind:value="{pattern}" labelText="패턴" />
</div>

<Slider
  labelText="스피드"
  hideTextInput
  bind:value="{speed}"
  fullWidth
  min="{10}"
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
  <div id="modal-container">
    <DataTable bind:headers bind:rows class="mauto" />
    <Rubiks bind:cubeMethod bind:speed></Rubiks>
  </div>
</Modal>
{/if}

<button class="main-btn" on:click="{calculate}">계산하기</button>
