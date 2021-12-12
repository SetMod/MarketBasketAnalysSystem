<template>
  <div>
    <img v-bind:src="imageUrl" class="img-fluid" alt="Transactions per month" />
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import store from "../../store/index";
export default {
  name: "TransactionImage",
  store: store,
  computed: {
    ...mapGetters({
      imageUrl: "getTransactionImageUrl",
    }),
  },
};
</script>

<style>
</style>