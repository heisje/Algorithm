# 14:00:00 15:00:00 Database
# 12
# 13:59:58 [INFO] System ready
# 14:00:01 [INFO] System started
# 14:00:48 [INFO] Database started
# 14:15:00 [WARN] Network delay in the database
# 14:15:30 [ERROR] Database connection failed
# 14:20:45 [ERROR] Database connection failed
# 14:20:49 [ERROR] Database connection failed
# 14:30:00 [WARN] High memory usage
# 14:45:00 [ERROR] Database timeout
# 14:59:59 [ERROR] Database connection failed
# 15:00:00 [WARN] Database connection pool is almost full.
# 15:00:02 [WARN] Database connection pool is almost full.

# [INFO]:
# - 14:00:48 Database started

# [WARN]:
# - 14:15:00 Network delay in the database
# - 15:00:00 Database connection pool is almost full.

# [ERROR]:
# - 14:15:30 Database connection failed (x3)
# - 14:45:00 Database timeout
# - 14:59:59 Database connection failed

# 상수 세팅
INFO = '[INFO]'
WARN = '[WARN]'
ERROR ='[ERROR]'
CATEGORY = [INFO, WARN, ERROR]

# 결과값 세팅
result = dict()
for category in CATEGORY:
    result[category] = []

# 타이틀
firstLine = input().split(' ')
startTime = firstLine[0]
endTime = firstLine[1]
title = firstLine[2].lower()

# 캐시저장
cacheCategory = ''
cacheTxt = ''

# 파싱
def Parse(log):
    global cacheCategory, cacheTxt
    parts = log.split(' ', 2)

    time = parts[0]
    category = parts[1]
    txt = parts[2]
    
    if (time < startTime):
        return True
    elif endTime < time:
        return False
    
    if not (title in txt.lower()):
        return True

    if(cacheCategory.lower() == category.lower() and txt.lower() in cacheTxt.lower()):
        result[category][-1][2] += 1
        return 
    result[category].append([time,txt,1])
    cacheCategory = category
    cacheTxt = txt
    return 

# 내용
N = int(input())

for i in range(N):
    rs = Parse(input())
    if(rs is False):
        break

for category in CATEGORY:
    print(category+':')
    for li in result[category]:
        count_str = f" (x{li[2]})" if li[2] > 1 else ""
        print(f"- {li[0]} {li[1]}{count_str}")
    print('')





# 14:00:00 15:00:00 Database
# 12
# 13:59:58 [INFO] System ready