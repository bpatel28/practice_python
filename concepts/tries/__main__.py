from concepts.tries import Trie


trie = Trie()

trie.insert("Brijesh")
trie.insert("Brij")
trie.insert("Mukti")

trie.remove("Brij")

print("Brijesh" in trie)
print("Brij" in trie)
print("Mukti" in trie)
print("Muktia" in trie)



print(trie.is_sub_str("Brijesh"))
print(trie.is_sub_str("Brij"))
print(trie.is_sub_str("Mukt"))
print(trie.is_sub_str("Bri"))

