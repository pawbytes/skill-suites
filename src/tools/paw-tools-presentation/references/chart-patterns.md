# Chart.js Implementation Patterns

## Setup

Chart.js is loaded from CDN:
```html
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
```

## Bar Chart

Best for: Comparisons across categories

```html
<div class="chart-container">
  <canvas id="chart-market-share"></canvas>
</div>
<script>
  new Chart(document.getElementById('chart-market-share'), {
    type: 'bar',
    data: {
      labels: ['Us', 'Competitor A', 'Competitor B', 'Competitor C'],
      datasets: [{
        label: 'Market Share (%)',
        data: [22, 35, 18, 12],
        backgroundColor: [
          'var(--primary)',
          'var(--secondary)',
          'var(--secondary)',
          'var(--secondary)'
        ],
        borderWidth: 0,
        borderRadius: 4
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: true,
      plugins: {
        legend: { display: false },
        title: { 
          display: true, 
          text: 'Market Share by Brand',
          font: { size: 14, weight: '600' }
        }
      },
      scales: {
        y: { 
          beginAtZero: true,
          ticks: { callback: value => value + '%' }
        }
      }
    }
  });
</script>
```

## Line Chart

Best for: Trends over time

```html
<div class="chart-container">
  <canvas id="chart-revenue-trend"></canvas>
</div>
<script>
  new Chart(document.getElementById('chart-revenue-trend'), {
    type: 'line',
    data: {
      labels: ['Q1', 'Q2', 'Q3', 'Q4'],
      datasets: [{
        label: 'Revenue ($K)',
        data: [120, 145, 180, 210],
        borderColor: 'var(--primary)',
        backgroundColor: 'rgba(37, 99, 235, 0.1)',
        fill: true,
        tension: 0.3
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: { position: 'bottom' },
        title: { display: true, text: 'Quarterly Revenue Growth' }
      },
      scales: {
        y: { beginAtZero: true }
      }
    }
  });
</script>
```

## Pie / Doughnut Chart

Best for: Proportions, market share, budget allocation

```html
<div class="chart-container">
  <canvas id="chart-budget"></canvas>
</div>
<script>
  new Chart(document.getElementById('chart-budget'), {
    type: 'doughnut',
    data: {
      labels: ['Paid Search', 'Social', 'Display', 'Content', 'Other'],
      datasets: [{
        data: [35, 25, 20, 15, 5],
        backgroundColor: [
          'var(--primary)',
          'var(--secondary)',
          'var(--accent)',
          '#10b981',
          '#94a3b8'
        ],
        borderWidth: 0
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: { position: 'right' },
        title: { display: true, text: 'Budget Allocation' }
      }
    }
  });
</script>
```

## Horizontal Bar Chart

Best for: Ranking, performance comparison

```html
<div class="chart-container">
  <canvas id="chart-performance"></canvas>
</div>
<script>
  new Chart(document.getElementById('chart-performance'), {
    type: 'bar',
    data: {
      labels: ['Email', 'Organic Search', 'Paid Search', 'Social', 'Direct'],
      datasets: [{
        label: 'Conversion Rate (%)',
        data: [5.2, 4.8, 3.9, 2.1, 1.8],
        backgroundColor: 'var(--primary)',
        borderWidth: 0,
        borderRadius: 4
      }]
    },
    options: {
      indexAxis: 'y',
      responsive: true,
      plugins: {
        legend: { display: false },
        title: { display: true, text: 'Conversion Rate by Channel' }
      },
      scales: {
        x: { 
          beginAtZero: true,
          ticks: { callback: value => value + '%' }
        }
      }
    }
  });
</script>
```

## Scatter Plot

Best for: Correlations, two-variable relationships

```html
<div class="chart-container">
  <canvas id="chart-correlation"></canvas>
</div>
<script>
  new Chart(document.getElementById('chart-correlation'), {
    type: 'scatter',
    data: {
      datasets: [{
        label: 'Ad Spend vs Revenue',
        data: [
          { x: 10, y: 45 },
          { x: 15, y: 52 },
          { x: 20, y: 68 },
          { x: 25, y: 75 },
          { x: 30, y: 89 }
        ],
        backgroundColor: 'var(--primary)',
        pointRadius: 6
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: { display: false },
        title: { display: true, text: 'Ad Spend vs Revenue Correlation' }
      },
      scales: {
        x: { 
          title: { display: true, text: 'Ad Spend ($K)' },
          beginAtZero: true 
        },
        y: { 
          title: { display: true, text: 'Revenue ($K)' },
          beginAtZero: true 
        }
      }
    }
  });
</script>
```

## Multi-Dataset Comparison

Best for: Before/after, year-over-year

```html
<div class="chart-container">
  <canvas id="chart-comparison"></canvas>
</div>
<script>
  new Chart(document.getElementById('chart-comparison'), {
    type: 'bar',
    data: {
      labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
      datasets: [
        {
          label: '2024',
          data: [65, 72, 68, 85, 92, 88],
          backgroundColor: 'var(--secondary)'
        },
        {
          label: '2025',
          data: [78, 85, 92, 105, 118, 125],
          backgroundColor: 'var(--primary)'
        }
      ]
    },
    options: {
      responsive: true,
      plugins: {
        legend: { position: 'top' },
        title: { display: true, text: 'YoY Performance Comparison' }
      },
      scales: {
        y: { beginAtZero: true }
      }
    }
  });
</script>
```

## Styling Guidelines

- **Primary data point:** Use `var(--primary)` color
- **Secondary/comparison:** Use `var(--secondary)` or muted colors
- **Highlight:** Use `var(--accent)` for emphasis
- **Border radius:** 4px for modern look
- **Legend position:** Bottom for wide charts, right for pie/doughnut
- **Title:** Always include for context