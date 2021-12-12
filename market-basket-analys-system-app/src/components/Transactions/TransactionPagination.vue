<template>
  <nav aria-label="Page navigation">
    <ul class="pagination justify-content-center">
      <li class="page-item">
        <button class="page-link text-black" @click="getPreviousPage">
          Previous
        </button>
      </li>
      <li class="page-item">
        <button class="page-link text-black" @click="getNextPage">Next</button>
      </li>
    </ul>
  </nav>
</template>

<script>
// import store from "../../store/index";
import { mapActions } from "vuex";
export default {
  methods: {
    ...mapActions({
      getNextPage: "transactions/getNextPage",
      getPreviousPage: "transactions/getPreviousPage",
    }),
  },
};
</script>

<style>
</style>