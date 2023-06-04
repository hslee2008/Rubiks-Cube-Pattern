<script>
  import {
    TextInput,
    Modal,
    ModalBody,
    DataTable
  } from 'carbon-components-svelte'
  import Cube from 'rubiks-cube'

  let pattern = 'R R U U'
  let moveCount = 0
  let opened = false

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

    let moveCount = 1
    while (!patternCube.isSolved()) {
      patternCube.scramble(pattern)
      moveCount++
    }

    return moveCount
  }

  function calculate() {
    opened = true

    moveCount = calculateMovesToFinishPattern(pattern)
  }
</script>

<div class="mb20">
  <h1>반복 횟수 계산기</h1>
</div>

<div class="mb20">
  <TextInput bind:value="{pattern}" labelText="패턴" />
</div>

<Modal
  bind:open="{opened}"
  modalHeading="반복 횟수 계산기"
  passiveModal
  selectorPrimaryFocus=".bx--modal-content"
>
  <DataTable bind:headers bind:rows />
</Modal>

<button class="main-btn" on:click="{calculate}">계산하기</button>
