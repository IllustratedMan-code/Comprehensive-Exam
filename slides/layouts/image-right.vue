<script setup lang="ts">
import { computed } from 'vue'
import { resolveAssetUrl } from '../layoutHelper.ts'

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

const i = computed(() => resolveAssetUrl(props.image)) 
</script>

<template>
  <div class="grid grid-cols-2 w-full h-full auto-rows-fr">
    <div class="slidev-layout default" :class="props.class">
      <slot />
    </div>
    <div class="p-3 w-full h-full flex flex-col items-center justify-center">
	 <img :src="i" class="max-w-full max-h-full min-h-0  -z-10" />
 	 <div class=" text-sm text-left opacity-70">
              <slot name="caption" />
      	 </div>
    </div>
  </div>
</template>