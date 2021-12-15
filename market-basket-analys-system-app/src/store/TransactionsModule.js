import axios from "axios";
export default {
    namespaced: true,
    state: {
        transactions: [],
        isLoaded: false,
        errorMsg: "",
        pageSize: 20,
        pageNumber: 1,
        sortIndex: 0
      },
      mutations: {
        setTransactions(state, transactions) {
          console.log('Setting transactions...');
          state.transactions = transactions
          console.log('Transactions is set.');
        },
        setLoaded(state, isLoaded) {
          console.log('Setting isLoaded...');
          state.isLoaded = isLoaded
          console.log(`IsLoaded is set to: ${state.isLoaded}`);
        },
        setError(state, errorMsg) {
          console.log('Setting errorMsg...');
          state.errorMsg = errorMsg
          console.log(`ErrorMsg is set to: ${state.errorMsg}`);
        },
        incrementPageNumber(state){
          console.log('Incrementing pageNumber...');
          state.pageNumber += 1
          console.log(`PageNumber is incremented to: ${state.pageNumber}`);
        },
        decrementPageNumber(state){
          if (state.pageNumber > 1){
            state.pageNumber -= 1
          }
        },
        setSortIndex(state,sortIndex){
          state.sortIndex = sortIndex
        }
      },
      getters:{
        getSortedTransactions(state){
          if (typeof state.transactions[0][state.sortIndex] ===	"string" ){
            return [...state.transactions].sort((tr1,tr2)=>tr1[state.sortIndex]?.localeCompare(tr2[state.sortIndex])) 
          } else if (typeof state.transactions[0][state.sortIndex] === "number"){
            return [...state.transactions].sort((tr1,tr2)=>tr2[state.sortIndex] - tr1[state.sortIndex])
          } else {
            return [...state.transactions].sort()
          }
        },
        // getSerachedTransaction(state, getters){
        //   return getters.getSortedTransactions.filter(trans => {})
        // }
      },
      actions: {
        async getTransactions({commit,  rootGetters }) {
            console.log('Fetching transactions...');
            commit('setTransactions', [])
            commit('setLoaded', false)
            commit('setError', '')
            console.log(rootGetters.getTransactionsUrl);
            await axios
              .get(rootGetters.getTransactionsUrl)
              .then((res) => {
                console.log('Transactions fetched...');
                commit('setTransactions', res.data)
                commit('setLoaded', true)
                commit('setError', '')
              })
              .catch((err) => {
                console.error(err);
                commit('setError', err)
              });
            },
          async getNextPage({commit, rootGetters}){
            console.log('Fetching next transactions page...');
            commit('setTransactions', [])
            commit('setLoaded', false)
            commit('setError', '')
            commit('incrementPageNumber')
            await axios
              .get(rootGetters.getTransactionsUrl)
              .then((res) => {
                console.log('Transactions fetched...');
                commit('setTransactions', res.data)
                commit('setLoaded', true)
                commit('setError', '')
              })
              .catch((err) => {
                console.error(err);
                commit('setError', err)
              });
      
          },
          async getPreviousPage({commit, rootGetters}){
            commit('setTransactions', [])
            commit('setLoaded', false)
            commit('setError', '')
            commit('decrementPageNumber')
            console.log('Fetching previous transactions page...');
            await axios
              .get(rootGetters.getTransactionsUrl)
              .then((res) => {
                console.log('Transactions fetched...');
                commit('setTransactions', res.data)
                commit('setLoaded', true)
                commit('setError', '')
              })
              .catch((err) => {
                console.error(err);
                commit('setError', err)
              });
          }
      },
      modules: {
      }
    }