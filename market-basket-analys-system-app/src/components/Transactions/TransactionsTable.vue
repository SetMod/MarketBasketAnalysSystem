<template>
  <h2 class="py-3 mt-3">Transactions</h2>
  <div class="table-responsive overflow-scroll">
    <table class="table table-striped table-hover table-sm table">
      <thead>
        <tr>
          <th scope="col">CostPerItem</th>
          <th scope="col">Country</th>
          <th scope="col">ItemCode</th>
          <th scope="col">ItemDescription</th>
          <th scope="col">NumberOfItemsPurchased</th>
          <th scope="col">TransactionId</th>
          <th scope="col">TransactionTime</th>
          <th scope="col">UserId</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(transaction, key1) in transactions" :key="key1">
          <td v-for="(val, key2) in transaction" :key="key2">{{ val }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "TransactionsTable",
  props: {
    transactions: {
      type: Array,
      required: true,
    },
  },
};
</script>

<style>
</style>