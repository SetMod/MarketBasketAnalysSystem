<template>
  <div class="transactions">
    <TransactionsList />
  </div>
</template>

<script>
import TransactionsList from "../components/TransactionsList.vue";
export default {
  name: "Transactions",
  components: {
    TransactionsList,
  },
};
</script>

<style>
.transactions {
  font-size: 20px;
}
</style>