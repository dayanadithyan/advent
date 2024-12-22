
def extract(text):

    patterns = []
    i = 0

    while i < len(text):

        start = text.find('mul(', i)
        if start == -1:
            break
        
        end = text.find(')', start)
        if end == -1:
            break
        
        nums = text[start+4:end].split(',')
        
        if (len(nums) == 2 and 
            all(num.strip().isdigit()
            and 1 <= len(num.strip()) <= 3 for num in nums)):
            patterns.append(f"mul({nums[0]},{nums[1]})")
        
        i = end + 1
    
    return patterns


with open('input.txt', 'r') as f:
    lines = f.read()

result = extract(lines)

nums = [item.replace('mul', '').strip('()') for item in result]

result2 = [(int(element1), int(element2)) for element1, element2 in (s.split(',') for s in nums)]

adds = [num1 * num2 for num1, num2 in result2]

print(type(adds))

answer = sum(adds)

print(answer)