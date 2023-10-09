import pandas as pd
import plotly.graph_objs as go
import plotly.subplots as sp

# Load your dataset from an Excel file
df = pd.read_excel('tasks_sample.xlsx')

# Convert the 'Duration (seconds)' column to Timedelta
df['Duration (seconds)'] = pd.to_timedelta(df['Duration (seconds)'])

# Create a subplot for the Gantt chart
fig = sp.make_subplots(rows=1, cols=1, subplot_titles=["Gantt Chart"])

# Define the Gantt chart
for index, row in df.iterrows():
    duration_seconds = row['Duration (seconds)'].total_seconds()
    fig.add_trace(
        go.Bar(
            y=[row['Task Name']],  # Adjust the column name here
            x=[row['Start DateTime']],
            orientation='h',
            width=duration_seconds,
            name=row['Task Name'],  # Adjust the column name here
        )
    )

# Customize the layout of the Gantt chart
fig.update_layout(
    title="<b>Gantt Chart</b>",
    height=600,
    showlegend=False,
)

# Show the Gantt chart
fig.show()

# Create a separate table figure
table_trace = go.Table(
    header=dict(values=["Task Label", "Task Name", "Start DateTime", "End DateTime", "Duration (seconds)"]),
    cells=dict(values=[df['Task Label'], df['Task Name'], df['Start DateTime'], df['End DateTime'], df['Duration (seconds)']]),
)

table_fig = go.Figure(data=[table_trace])
table_fig.update_layout(
    title="<b>Data Table</b>",
)

# Show the table figure
table_fig.show()
