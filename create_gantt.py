import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Read the data from 'tasks_sample.xlsx'
df = pd.read_excel('tasks_sample.xlsx')

# Convert columns to datetime objects
df['Start'] = pd.to_datetime(df['Start DateTime'])
df['Finish'] = pd.to_datetime(df['End DateTime'])
df['Task'] = df['Task Name']

# Calculate statistics
statistics_df = df.groupby('Task Label')['Duration (hours)'].agg(['mean', 'max', 'min']).reset_index()

# Define custom colors
colors = {
    'Planning Phase': 'rgb(30, 144, 255)',
    'Design Phase': 'rgb(0, 0, 128)',
    'Development Phase': 'rgb(95, 158, 160)',
    'Testing Phase': 'rgb(255, 69, 0)',
    'Deployment Phase': 'rgb(50, 205, 50)',
    'Monitoring Phase': 'rgb(139, 0, 139)'
}

fig_gantt = ff.create_gantt(
    df,
    colors=colors,
    index_col='Task Label',
    group_tasks=True,
    show_colorbar=True,
    bar_width=0.2,
    showgrid_x=True,
    showgrid_y=True,
    title='Gantt Chart'
)

# Create a bar chart for statistics
bar_chart = go.Figure()
bar_chart.add_trace(go.Bar(
    x=statistics_df['Task Label'],
    y=statistics_df['mean'],
    name='Average Duration',
    marker_color='rgb(30, 144, 255)'
))
bar_chart.add_trace(go.Bar(
    x=statistics_df['Task Label'],
    y=statistics_df['max'],
    name='Max Duration',
    marker_color='rgb(0, 0, 128)'
))
bar_chart.add_trace(go.Bar(
    x=statistics_df['Task Label'],
    y=statistics_df['min'],
    name='Min Duration',
    marker_color='rgb(95, 158, 160)'
))

# Create subplots with shared y-axes
fig = make_subplots(rows=1, cols=2, subplot_titles=("Gantt Chart", "Overview"))

for trace in fig_gantt.data:
    fig.add_trace(trace, row=1, col=1)
    print(fig_gantt.data)

# Add your second figure (fig2) to the second subplot
for trace in bar_chart.data:
    fig.add_trace(trace, row=1, col=2)

# Customize the chart appearance
fig_gantt.update_yaxes(categoryorder="total ascending")
fig_gantt.update_xaxes(title="Timeline")
fig_gantt.update_yaxes(title="Task Name")
fig_gantt.update_layout(
    title="Gantt Chart",
    font=dict(
        family="Arial",
        size=14,
        color="darkgray"
    ),
    showlegend=True,
    legend_title_text="Stage",
    legend_font=dict(size=12),
    legend_traceorder="reversed",
    barmode='group',  # Stack or group the bars in the bar chart
    xaxis=dict(domain=[0, 0.7]),  # Adjust the domain to make the Gantt chart smaller
    xaxis2=dict(domain=[0.75, 1.0]),  # Adjust the domain for the statistics chart
)

# Show the chart
fig.show()
