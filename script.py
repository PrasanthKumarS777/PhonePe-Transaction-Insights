from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import inch

pdf = SimpleDocTemplate('PhonePe_Project_Report.pdf', pagesize=A4,
                        rightMargin=50, leftMargin=50, topMargin=50, bottomMargin=50)
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='CenterTitle', parent=styles['Title'], alignment=TA_CENTER, spaceAfter=18))
styles.add(ParagraphStyle(name='Body2', parent=styles['BodyText'], leading=15, spaceAfter=10))

def h(text):
    return [Spacer(1, 0.1 * inch), Paragraph(text, styles['Heading1']), Spacer(1, 0.05 * inch)]

def p(text):
    return [Paragraph(text, styles['Body2']), Spacer(1, 0.05 * inch)]

story = []
story.append(Paragraph('PhonePe Transaction Insights - Project Report', styles['CenterTitle']))
story.append(Spacer(1, 0.2 * inch))

story += h('How I Approached This')
story += p('I picked PhonePe transaction data because honestly, payments data from India is something I find genuinely interesting. The way people transact across different states and categories tells a lot more than just numbers -- it reflects spending habits, regional economic patterns, and how digital payments have grown in this country over the last few years.')
story += p("I started by just pulling the raw data and looking at it. The dataset had transaction records across 36 Indian states and union territories, and the first thing I noticed was that the data wasn't clean -- there were inconsistencies in state names, some null values in the category columns, and the date fields needed parsing before I could do anything meaningful with them. So before any analysis, I spent a good chunk of time on the ETL side.")
story += p("Once the data was clean, I loaded it into a PostgreSQL database. I designed 9 tables keeping normalization in mind -- things like separating transactions, users, devices, and location data so queries wouldn't be slow or messy. The total data I was working with was around 150MB which isn't massive but it was enough to make poor schema design noticeably painful, so I was careful about indexing and joins from the start.")

story += h('What I Actually Did')
story += p('Most of the work fell into three areas -- SQL analysis, exploratory data analysis in Python, and building the dashboard.')
story += p("For the SQL part, I wrote 9 business-focused queries. These weren't just SELECT * type things -- I was looking at things like which states had the highest transaction volumes, what the average transaction value looked like across different payment categories, and how growth trended quarter over quarter. Writing these queries made me think like someone in a business intelligence role rather than just a developer.")
story += p("The EDA part in Python was where I spent the most time. I built 22 visualizations in total -- covering time-series trends, geo maps showing state-level distribution, category breakdowns, and user-device analysis. I used matplotlib and seaborn mostly, and for the geo plots I used folium. Some charts didn't turn out useful the first time so I redid them -- the geo heatmap especially took a few tries to make readable.")
story += p("The dashboard was built in Streamlit and deployed to Streamlit Cloud. I wanted it to actually be interactive, not just static images, so I added filters for state, date range, and category. The goal was that someone with no coding background should be able to open it and draw conclusions within a few minutes.")

story += h('Insights I Found')
story += p("A few things stood out to me during the analysis that I wasn't expecting going in.")
story += p("First -- Maharashtra, Karnataka, and Telangana together accounted for a disproportionately large share of total transaction volume. This wasn't surprising on its own but what was interesting is that when I looked at average transaction value, smaller states like Goa and Sikkim had higher per-transaction amounts. So volume and value don't always move together -- which has real implications for how you'd prioritize merchant acquisition if you were a fintech.")
story += p("Second -- merchant payments and recharges/bill payments dominated the category breakdown. Peer-to-peer transfers were high in frequency but lower in average value, which makes sense. What I found interesting was the spike in bill payment transactions in the March-April window every year -- likely driven by end-of-financial-year utility settlements and insurance renewals.")
story += p("Third -- Android devices completely dominated across all states with very little variation. But in metro cities the iOS share was noticeably higher than the national average. This kind of device segmentation is something a product team would actually care about for UI prioritization.")
story += p("Fourth -- transaction growth was not linear. There were specific quarters that showed sharp jumps, likely tied to cashback campaigns or government initiatives like UPI incentive programs. The time-series analysis made these inflection points very visible.")

story += h('What Could Be Done Next')
story += p("There is a lot of room to take this further and I have a few directions in mind.")
story += p("The most obvious next step is adding predictive modeling -- using the historical transaction trends to forecast state-level or category-level volumes for the next quarter. A simple ARIMA or Prophet model would work here and wouldn't be overkill for the data size.")
story += p("Another thing I'd like to add is anomaly detection. Right now the dashboard just shows you what happened, but it would be much more useful if it could flag unusual spikes or drops automatically. Something like an Isolation Forest or even a Z-score based alert on rolling averages could work well.")
story += p("I also want to bring in external data -- things like state-level GDP, internet penetration rates, and population density -- and see how well PhonePe adoption correlates with those. That would make the geo analysis a lot richer and move it from descriptive to actually explanatory.")
story += p("On the dashboard side, I'd like to add a user cohort analysis feature -- tracking how transaction behavior changes for the same user segment over time. That is something that is hard to do with aggregate data but would be possible with a more granular dataset.")

story += h('What I Took Away From This')
story += p("Honestly this project taught me more about how to think about data than about any specific tool. The SQL schema design forced me to think ahead about how the data would be queried. The EDA made me realize how easy it is to build charts that look nice but don't say anything -- I had to keep asking myself: so what does this actually tell someone?")
story += p("The dashboard deployment was also a good reminder that analysis only has value if someone can actually use it. A notebook on your local machine helps nobody. Getting it live on Streamlit Cloud, with filters and real data, is what makes it a real project rather than just an exercise.")
story += p("If I were to do it again I'd probably start the schema design on paper before touching any code. I made a couple of structural decisions early that I had to backtrack on, and that cost time. But overall I'm happy with where it landed.")

pdf.build(story)
print('PDF saved')
