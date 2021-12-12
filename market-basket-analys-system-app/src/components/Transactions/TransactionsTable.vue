<template>
  <div class="table-responsive overflow-scroll">
    <table class="table table-striped table-hover table-sm table">
      <thead>
        <tr>
          <th
            scope="col"
            class="clickable"
            v-for="(header, key) in headers"
            :key="key"
            @click="getHeader"
          >
            {{ header }}
          </th>
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
import { mapGetters, mapMutations, mapState } from "vuex";
import store from "../../store/index";
export default {
  name: "TransactionsTable",
  data() {
    return {
      headers: [
        "CostPerItem",
        "Country",
        "ItemCode",
        "ItemDescription",
        "NumberOfItemsPurchased",
        "TransactionId",
        "TransactionTime",
        "UserId",
      ],
    };
  },
  store: store,
  props: {
    transactions: {
      type: Array,
      required: true,
    },
  },
  computed: {
    ...mapState({
      sortIndex: (state) => state.transactions.sortIndex,
    }),
    ...mapGetters({
      sortedTransactions: "transactions/getSortedTransactions",
    }),
  },
  methods: {
    ...mapMutations({
      setSortIndex: "transactions/setSortIndex",
      setTransactions: "transactions/setTransactions",
    }),
    getHeader(e) {
      this.setSortIndex({ index: e.target.cellIndex });
      this.setTransactions({ data: this.sortedTransactions });
    },
  },
};
</script>

<style>
.clickable {
  cursor: pointer;
}
</style>