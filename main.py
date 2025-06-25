def rabin_karp(haystack, needle):
   if not haystack or not needle:
       return []


   result = []
   base = 256
   prime = 101


   def calculate_hash(string, length):
       hash_value = 0
       for index in range(length):
           hash_value = (hash_value * base + ord(string[index])) % prime
       return hash_value


   haystack_length = len(haystack)
   needle_length = len(needle)


   needle_hash = calculate_hash(needle, needle_length)
   haystack_hash = calculate_hash(haystack, needle_length)


   for i in range(haystack_length - needle_length + 1):
       if needle_hash == haystack_hash and needle == haystack[i:i + needle_length]:

            result.append(i)


       if i < haystack_length - needle_length:
           haystack_hash = (base * (haystack_hash - ord(haystack[i]) * pow(base, needle_length - 1, prime)) + ord(haystack[i + needle_length])) % prime                        

   return result
