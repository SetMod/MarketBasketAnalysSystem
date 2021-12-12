<template>
  <div
    class="collapse navbar-collapse justify-content-center"
    id="navbarSupportedContent"
  >
    <slot></slot>
  </div>
  <button
    class="navbar-toggler my-2"
    type="button"
    data-bs-toggle="collapse"
    data-bs-target="#navbarSupportedContent"
    aria-controls="navbarSupportedContent"
    aria-expanded="false"
    aria-label="Toggle navigation"
  >
    <span class="navbar-toggler-icon"></span>
  </button>
</template>

<script>
export default {};
</script>

<style>
</style>