import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid
} from "recharts";

function PolicyShiftChart({ data }) {
  return (
    <div>
      <h2>Policy Shift Analysis</h2>

      <BarChart
        width={500}
        height={300}
        data={data}
      >
        <CartesianGrid strokeDasharray="3 3" />

        <XAxis dataKey="topic" />

        <YAxis />

        <Tooltip />

        <Bar dataKey="change" />
      </BarChart>
    </div>
  );
}

export default PolicyShiftChart;