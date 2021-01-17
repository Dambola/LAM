<template>
  <tr @click="openDetailMusic">
    <td class="text-left">
      <div class="text-subtitle1"><strong>{{ music.name }}</strong></div>
      <small>{{ music.author }}</small>
    </td>
    <td class="text-right">
      <div>{{ getTypeName(music.type1) }}</div>
      <div>{{ getTypeName(music.type2) }}</div>
      <div>{{ getTypeName(music.type3) }}</div>
    </td>
  </tr>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'

  export default {
    props : ['music', 'id'],
    computed : {
      ...mapGetters('types', ['types']),
    },
    methods : {
      ...mapActions('musics', ['updateMusic', 'deleteMusic']),
      promptToDelete (id) {
        this.$q.dialog({
          title: 'Confirm',
          message: 'Really delete?',
          ok: {
            push: true
          },
          cancel: {
            color: 'negative'
          },
          persistent: true
        }).onOk(() => {
          this.deleteMusic(id)
        })
      },
      openDetailMusic () {
        this.$emit('openDetailMusic',this.id)
      },
      getTypeName(type) {
        if (type !== null && this.types[type] !== null) {
          return this.types[type].name;
        }
        return '';
      }
    }
  }
</script>

<style lang="scss">
</style>