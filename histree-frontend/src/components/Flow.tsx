import React from "react";
import ReactFlow, { Controls, Background } from "reactflow";
import "reactflow/dist/style.css";

const nodes = [
	{
		id: "1",
		position: { x: 0, y: 0 },
		data: { label: "Hello" },
		type: "input",
	},
];

const Flow = () => {
	return (
		<div style={{ height: "100%" }}>
			<ReactFlow nodes={nodes}>
				<Background />
				<Controls />
			</ReactFlow>
		</div>
	);
};

export default Flow;
