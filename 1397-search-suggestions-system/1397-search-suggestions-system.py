class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res = []
        temp = products
        for i in range(len(searchWord)):


            part = []
            for product in temp:
                if i<len(product) and searchWord[i] == product[i]:
                    part.append(product)

            if len(part) > 3:
                res.append(part[:3])
            else:
                res.append(part[:])
    
            temp = part

        return res
            