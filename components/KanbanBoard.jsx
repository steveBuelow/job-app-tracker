import { useState } from "react";
import Column from "./Column";
import JobCard from "./JobCard";

export default function KanbanBoard() {
    const [jobs, setJobs] = useState([
        {id: 1, title: "Google SWE Intern", status: "applied"},
        {id: 1, title: "Amazon Backend Role", status: "interview"},
    ]);

    const moveJob = (id, newStatus) => {
        setJobs(prev =>
            prev.map(job =>
                job.id === id ? { ...job, status: newStatus } : job
            )
        )
    };
};

  return (
    <div style={{ display: "flex", gap: "20px" }}>
      <Column title="Applied" status="applied" jobs={jobs} moveJob={moveJob} />
      <Column title="Interview" status="interview" jobs={jobs} moveJob={moveJob} />
      <Column title="Offer" status="offer" jobs={jobs} moveJob={moveJob} />
    </div>
  );
}
