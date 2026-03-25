from flask import Flask, render_template

app = Flask(__name__)

funds = [
    {
     "name":"EdgePoint Canadian Portfolio",  
     "focus":"Canadian companies with strong fundamentals and long term growth potential, purchased at prices below their perceived value", 
     "geography": "Primarily Canadian companies, limited international exposure (typically less than 15%)",
     "income":False,
     "accredited_only":False,
     "min_investment":None,
     "investor_profile":"Investors focused on long term growth rather than regular payouts, such as someone in their early career building wealth",
     "not_for":"Investors who rely on steady income or need regular cash flow from their investments",
     "edgepoint_edge":"Avoids the Canadian oligopolies that dominate the TSX, like the Big 6 banks, Rogers and Bell, and instead focuses on undervalued mid-cap Canadian businesses that are typically overlooked.",
     "tradeoff":"You're giving up global diversification in exchange for concentrated exposure to undervalued Canadian businesses with no currency risk",
    },
    {
        "name":"EdgePoint Canadian Growth & Income Portfolio",
        "focus":"Combines Canadian equity with fixed income to grow your money and pay you along the way, without having to sell investments to access cash",
        "geography":"Primarily Canadian businesses, with foreign securities capped at 20%",
        "income":True,
        "accredited_only":False,
        "min_investment":None,
        "investor_profile":"Someone in their 50s who is still working but wanting their portfolio to start generating cash, or a retiree with a pension covering basics who wants their investments to keep growing on top",
        "not_for":"Someone who wants maximum long term growth and doesn't need income yet, or someone who needs large regular payouts immediately",
        "edgepoint_edge":"Holds significant cash when good opportunities aren't available rather than forcing bad investments just to stay fully invested",
        "tradeoff":"Giving up maximum long term growth in exchange for regular income and lower volatility during market downturns.",
    },
    {
        "name":"EdgePoint Global Portfolio",
        "focus":"Same bottom-up value approach as the Canadian Portfolio but applied globally, giving EdgePoint a much larger pool of undervalued businesses to choose from across different economies, industries and currencies.",
        "geography":"Global",
        "income":False,
        "accredited_only":False,
        "min_investment":None,
        "investor_profile":"A mid-career professional with a diversified income who wants global equity exposure without having to pick individual foreign stocks themselves.",
        "not_for":"Someone who wants Canadian-only exposure or is uncomfortable with currency risk — when the Canadian dollar strengthens, foreign returns take a hit when converted back to CAD.",
        "edgepoint_edge":"Doesn't chase Apple, Nvidia or Amazon like every other global fund, looks for undervalued businesses in markets most Canadian investors never think to look.",
        "tradeoff":"Giving up Canadian-only familiarity and currency certainty in exchange for access to a much larger pool of undervalued global businesses.",
    },
    {
        "name": "EdgePoint Global Growth & Income Portfolio",
        "focus": "Global equity and fixed income combined. Grows your money through international businesses while the fixed income portion generates regular income, so you don't have to sell investments to access cash.",
        "geography": "Global",
        "income": True,
        "accredited_only": False,
        "min_investment": None,
        "investor_profile": "A Canadian investor in their 50s who wants global exposure but is starting to think about cash flow, not ready to stop growing their money but wants the portfolio to start paying them.",
        "not_for": "Someone who wants pure global growth and doesn't need income yet, or someone who wants Canadian-only exposure without currency risk.",
        "edgepoint_edge": "Buys overlooked global businesses that the market is undervaluing: Mattel, Dollar Tree, Roche. Not the household names dominating everyone else's portfolio.",
        "tradeoff": "Giving up the full upside of a pure global equity strategy in exchange for regular income and lower volatility during market downturns.",
    },
    {
        "name": "EdgePoint Monthly Income Portfolio",
        "focus": "Primarily Canadian fixed income securities focused on generating reliable monthly cash flow through coupon payments and interest, with the potential for some growth over time.",
        "geography": "Primarily Canadian",
        "income": True,
        "accredited_only": False,
        "min_investment": None,
        "investor_profile": "Someone in retirement who wants their portfolio to generate consistent monthly income, having moved from building wealth to relying on it for a predictable income stream.",
        "not_for": "Anyone with a long time horizon who doesn't need cash flow yet — the returns are modest and you give up significant growth potential.",
        "edgepoint_edge": "Unlike most fixed income funds that charge the same fee no matter what, EdgePoint charges less when interest rates are low and it's harder to earn a return, they only make more when the environment makes it easier to.",
        "tradeoff": "Giving up long term growth and equity upside in exchange for predictable monthly income and the lowest volatility of all six portfolios.",
    },
    {
        "name": "EdgePoint Opportunistic Credit Portfolio",
        "focus": "Invests primarily in corporate debt, looking for mispriced bonds in companies that are misunderstood or out of favour — generates income through coupon payments with some capital appreciation.",
        "geography": "Global",
        "income": True,
        "accredited_only": True,
        "min_investment": "$20,000",
        "investor_profile": "A high-net-worth accredited investor who wants fixed income returns that beat traditional bonds without taking on full equity risk — someone with at least $1M in financial assets who can afford to lock up their money for a quarter at a time.",
        "not_for": "Retail investors — this fund is only available to accredited investors. Also not for anyone who might need to access their money quickly since you can only redeem quarterly.",
        "edgepoint_edge": "Zero management fee — EdgePoint only makes money when investors do. Most funds charge a management fee regardless of performance. Here, if the fund doesn't make money, neither does EdgePoint.",
        "tradeoff": "Giving up daily liquidity and accessibility in exchange for higher fixed income returns than traditional bond funds — you can only redeem quarterly and must qualify as an accredited investor to access it at all.",
    },

    

]

@app.route("/")
def index():
    return render_template("index.html", funds=funds)

if __name__ == "__main__":
    app.run(debug=True)    

