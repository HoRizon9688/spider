import re

find_date = re.compile(r'<b>(.*)</b>')
find_value = re.compile(r'<span>(.*)</span>')


text = '''<table class="table table-bordered table-striped">
    <thead>
    <tr>
        <th>IP</th>
        <th>PORT</th>
        <th>匿名度</th>
        <th>类型</th>
        <th>位置</th>
        <th>响应速度</th>
        <th>最后验证时间</th>
    </tr>
    </thead>
    <tbody>

    <tr>
        <td data-title="IP">59.66.19.53</td>
        <td data-title="PORT">7890</td>
        <td data-title="匿名度">高匿名</td>
        <td data-title="类型">HTTP</td>
        <td data-title="位置">中国 北京  </td>
        <td data-title="响应速度">0.2秒</td>
        <td data-title="最后验证时间">2021-11-29 16:31:01</td>
    </tr>

    <tr>
        <td data-title="IP">222.78.6.2</td>
        <td data-title="PORT">8083</td>
        <td data-title="匿名度">高匿名</td>
        <td data-title="类型">HTTP</td>
        <td data-title="位置">中国 福建 漳州 电信</td>
        <td data-title="响应速度">4秒</td>
        <td data-title="最后验证时间">2021-11-29 15:31:01</td>
    </tr>

    <tr>
        <td data-title="IP">111.231.86.149</td>
        <td data-title="PORT">7890</td>
        <td data-title="匿名度">高匿名</td>
        <td data-title="类型">HTTP</td>
        <td data-title="位置">中国 上海  </td>
        <td data-title="响应速度">4秒</td>
        <td data-title="最后验证时间">2021-11-29 14:31:01</td>
    </tr>

    <tr>
        <td data-title="IP">59.66.19.53</td>
        <td data-title="PORT">7890</td>
        <td data-title="匿名度">高匿名</td>
        <td data-title="类型">HTTP</td>
        <td data-title="位置">中国 北京  </td>
        <td data-title="响应速度">0.2秒</td>
        <td data-title="最后验证时间">2021-11-29 13:31:02</td>
    </tr>

    <tr>
        <td data-title="IP">140.246.208.23</td>
        <td data-title="PORT">8888</td>
        <td data-title="匿名度">高匿名</td>
        <td data-title="类型">HTTP</td>
        <td data-title="位置">中国 山东 潍坊 电信</td>
        <td data-title="响应速度">0.4秒</td>
        <td data-title="最后验证时间">2021-11-29 12:31:02</td>
    </tr>

    <tr>
        <td data-title="IP">8.136.6.248</td>
        <td data-title="PORT">7788</td>
        <td data-title="匿名度">高匿名</td>
        <td data-title="类型">HTTP</td>
        <td data-title="位置">中国   </td>
        <td data-title="响应速度">1秒</td>
        <td data-title="最后验证时间">2021-11-29 11:31:02</td>
    </tr>

    <tr>
        <td data-title="IP">103.216.103.25</td>
        <td data-title="PORT">80</td>
        <td data-title="匿名度">高匿名</td>
        <td data-title="类型">HTTP</td>
        <td data-title="位置">中国 香港 ofidc.com </td>
        <td data-title="响应速度">0.5秒</td>
        <td data-title="最后验证时间">2021-11-29 10:31:02</td>
    </tr>

    <tr>
        <td data-title="IP">114.116.225.188</td>
        <td data-title="PORT">7890</td>
        <td data-title="匿名度">高匿名</td>
        <td data-title="类型">HTTP</td>
        <td data-title="位置">中国 北京  </td>
        <td data-title="响应速度">0.2秒</td>
        <td data-title="最后验证时间">2021-11-29 09:31:01</td>
    </tr>

    <tr>
        <td data-title="IP">222.78.6.2</td>
        <td data-title="PORT">8083</td>
        <td data-title="匿名度">高匿名</td>
        <td data-title="类型">HTTP</td>
        <td data-title="位置">中国 福建 漳州 电信</td>
        <td data-title="响应速度">4秒</td>
        <td data-title="最后验证时间">2021-11-29 08:31:01</td>
    </tr>

    <tr>
        <td data-title="IP">221.125.138.189</td>
        <td data-title="PORT">8193</td>
        <td data-title="匿名度">高匿名</td>
        <td data-title="类型">HTTP</td>
        <td data-title="位置">中国 香港 hgc.com.hk </td>
        <td data-title="响应速度">0.8秒</td>
        <td data-title="最后验证时间">2021-11-29 07:31:01</td>
    </tr>

    <tr>
        <td data-title="IP">117.24.81.222</td>
        <td data-title="PORT">3256</td>
        <td data-title="匿名度">高匿名</td>
        <td data-title="类型">HTTP</td>
        <td data-title="位置">中国 福建 泉州 电信</td>
        <td data-title="响应速度">0.5秒</td>
        <td data-title="最后验证时间">2021-11-29 06:31:02</td>
    </tr>

    <tr>
        <td data-title="IP">27.203.138.113</td>
        <td data-title="PORT">8060</td>
        <td data-title="匿名度">高匿名</td>
        <td data-title="类型">HTTP</td>
        <td data-title="位置">山东省威海市  联通</td>
        <td data-title="响应速度">1秒</td>
        <td data-title="最后验证时间">2021-11-29 05:31:02</td>
    </tr>

    <tr>
        <td data-title="IP">58.215.201.98</td>
        <td data-title="PORT">56566</td>
        <td data-title="匿名度">高匿名</td>
        <td data-title="类型">HTTP</td>
        <td data-title="位置">江苏省无锡市  电信</td>
        <td data-title="响应速度">4秒</td>
        <td data-title="最后验证时间">2021-11-29 04:31:01</td>
    </tr>

    <tr>
        <td data-title="IP">111.231.86.149</td>
        <td data-title="PORT">7890</td>
        <td data-title="匿名度">高匿名</td>
        <td data-title="类型">HTTP</td>
        <td data-title="位置">中国 上海  </td>
        <td data-title="响应速度">4秒</td>
        <td data-title="最后验证时间">2021-11-29 03:31:01</td>
    </tr>

    <tr>
        <td data-title="IP">219.151.142.29</td>
        <td data-title="PORT">3128</td>
        <td data-title="匿名度">高匿名</td>
        <td data-title="类型">HTTP</td>
        <td data-title="位置">中国 重庆  电信</td>
        <td data-title="响应速度">1秒</td>
        <td data-title="最后验证时间">2021-11-29 02:31:01</td>
    </tr>

    </tbody>
</table>'''
data = find_date.findall(text)
value = find_value.findall(text)
for i, j in zip(data, value):
    print(i, j)
