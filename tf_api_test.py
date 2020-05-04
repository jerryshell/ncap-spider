from comment_list import get_comment_list_by_news_id
from tf_api import predict

# print('get_rank_news')
# news_list = get_rank_news()
# print('len(news_list) %s' % len(news_list))
#
# target_news = news_list[0]
# print(target_news)

print('get_comment_list_by_news_id')
# comment_list = get_comment_list_by_news_id(target_news['id'])

# 韩正在人民大会堂出席的开工仪式 背后有深意
# comment_list = get_comment_list_by_news_id('FARP2UFO051482MP')

# 4名儿童被埋记者采访遭殴打 官方:死者家属动的手
comment_list = get_comment_list_by_news_id('FAP6462T0001875P')

print('len(comment_list) %s' % len(comment_list))

target_comment = comment_list[0]
print(target_comment)

p_count = 0
n_count = 0
for index, comment in enumerate(comment_list):
    print('--- %s/%s %s' % (index + 1, len(comment_list), (index + 1) / len(comment_list) * 100))
    content = comment['content']
    print('评论内容: %s' % content)

    result = predict(content, 'Super@dmin', False, 0)
    print(result)
    if not result.get('ok', False):
        continue
    if result['p'] >= 60:
        p_count += 1
    elif result['n'] >= 60:
        n_count += 1
    print('正面评论计数 %s 负面评论计数 %s' % (p_count, n_count))
    count_sum = p_count + n_count
    if count_sum > 0:
        print('负面新闻概率 %s' % (n_count / count_sum * 100))
