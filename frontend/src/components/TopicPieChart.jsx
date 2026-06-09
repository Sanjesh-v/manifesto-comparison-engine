import {
  PieChart,
  Pie,
  Tooltip,
  Legend
} from "recharts";

function TopicPieChart({ data }) {
  return (
    <div>
      <h2>Topic Distribution</h2>

      <PieChart width={400} height={300}>
        <Pie
          data={data}
          dataKey="value"
          nameKey="name"
          outerRadius={100}
          label
        />

        <Tooltip />
        <Legend />
      </PieChart>
    </div>
  );
}

export default TopicPieChart;