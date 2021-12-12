<template>
  <button
    type="button"
    class="btn btn-dark btn-floating position-fixed btn-back-to-top"
    @click="backToTop"
    v-show="display"
  >
    Top
  </button>
</template>

<script>
export default {
  data() {
    return {
      display: true,
      distance: 250,
    };
  },
  methods: {
    scrollFunction() {
      if (
        document.body.scrollTop > this.distance ||
        document.documentElement.scrollTop > this.distance
      ) {
        this.display = true;
      } else {
        this.display = false;
      }
    },
    backToTop() {
      document.body.scrollTop = 0;
      document.documentElement.scrollTop = 0;
    },
  },
  mounted() {
    this.scrollFunction();
    window.addEventListener("scroll", this.scrollFunction);
  },
  unmounted() {
    window.removeEventListener("scroll", this.scrollFunction);
  },
};
</script>

<style>
.btn-back-to-top {
  bottom: 20px;
  right: 20px;
}
</style>