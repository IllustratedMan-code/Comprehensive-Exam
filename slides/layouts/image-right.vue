<script setup lang="ts">
import { computed } from 'vue'
import { handleBackground } from '../layoutHelper.ts'

const props = defineProps({
  image: {
    type: String,
  },
  class: {
    type: String,
  },
  backgroundSize: {
    type: String,
    default: 'contain',
  },
})

const style = computed(() => handleBackground(props.image, false, props.backgroundSize))
</script>

<template>
  <div class="grid grid-cols-2 w-full h-full auto-rows-fr">
    <div class="slidev-layout default" :class="props.class">
      <slot />
    </div>
    <div class="w-full h-full flex flex-col items-center justify-center">
	 <img :src="props.image" class="p-5 max-w-full max-h-80%  -z-10" />
 	 <div class="p-2 text-sm text-center opacity-70">
              <slot name="caption" />
      	 </div>
    </div>
  </div>
</template>