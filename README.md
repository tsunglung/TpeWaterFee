<a href="https://www.buymeacoffee.com/tsunglung" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="30" width="120"></a>
Home assistant support for TpeWater Fee

The method was provided by [Jason Lee](https://www.dcard.tw/@jas0n.1ee.com).

***User the integration by your own risk***

## Install

You can install component with [HACS](https://hacs.xyz/) custom repo: HACS > Integrations > 3 dots (upper top corner) > Custom repositories > URL: `tsunglung/TpeWaterFee` > Category: Integration

Or manually copy `tpewater_fee` folder to `custom_components` folder in your config folder.

Then restart HA.

# Setup

You need to grab a cookie and two tokens.

**1. Basic steps for grabbing**

1. Open the development tools (use Google chrome/Microsoft Edge) [Crtl+Shift+I / F12]
2. Open the Network tab
3. Open the [TpeWater Fee Web site](https://webs.water.gov.taipei/apps/feequery), Enter the Water ID and input Verification code.
4. Search for "fee" (for me only two itemes shows up, choose the first one)
5. Go to "headers" -> "request headers"
6. copy the 24 characters like "xwu51weubdalqqkmnlizypxc" starting after "SessionId=" in the field (mark with a mouse and copy to clipboard)
7. Go to "headers" -> "from data"
8. copy the > 5308 characters like "\wXXXXXXXXXXXX....=" in the field "\__VIEWSTATE:"  (mark with a mouse and copy to clipboard)
9. copy the > 668 characters like "\wXXXXXXXXXXXX....." in the field "\__EVENTVALIDATION:"  (mark with a mouse and copy to clipboard)
   If the lenght of tokens are not right, do querying again.

# Config

![grabbing](grabbing.png)

**2. Please use the config flow of Home Assistant**


1. With GUI. Configuration > Integration > Add Integration > TpeWater Fee
   1. If the integration didn't show up in the list please REFRESH the page
   2. If the integration is still not in the list, you need to clear the browser cache.
2. Enter Water ID without dash.
3. Paste the cookie and viewstate token, validation toekn into the indicated field, all fields are Required.

# Notice
The cookie and tokens will expired after hours. If you saw the https_result is 403, you need get the new cookie and tokens again.
Then got to Configuration > Integration > TpeWater Fee > Options, enter the info of cookie and tokens.
