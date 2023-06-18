<script>
  import {
    TextInput,
    Modal,
    ModalBody,
    DataTable,
    Slider,
    OutboundLink
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

    try {
      setTimeout(() => cubeMethod.execute(completeMove), 200)
    } catch {
      setTimeout(() => cubeMethod.execute(completeMove), 500)
    }
  }

  function close() {
    openedCalc = false
  }
</script>

<div class="mb50">
  <h1 style="margin-bottom: 5px">패턴 반복 계산기</h1>
  <p class="mb10">패턴의 최소 반복 횟수 계산 프로그램</p>
  <OutboundLink href="https://jperm.net/3x3/moves">
    루빅스 큐브 표기법
  </OutboundLink>
</div>

<div class="mb20">
  <TextInput bind:value="{pattern}" labelText="루빅스 큐브 패턴 (표기법)" />
</div>

<Slider
  labelText="스피드"
  hideTextInput
  bind:value="{speed}"
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
    <DataTable bind:headers bind:rows />
    <Rubiks bind:cubeMethod bind:speed></Rubiks>
  </div>

  <button class="main-btn mt20" on:click="{close}">닫기</button>
</Modal>
{/if}

<button class="main-btn mt20" on:click="{calculate}">계산하기</button>
