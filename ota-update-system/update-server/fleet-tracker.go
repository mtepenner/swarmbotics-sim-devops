package updateserver

import (
	"sort"
	"sync"
	"time"
)

type VehicleRecord struct {
	VehicleID       string
	SoftwareVersion string
	Channel         string
	Partition       string
	Healthy         bool
	UpdatedAt       time.Time
}

type FleetTracker struct {
	mu       sync.RWMutex
	vehicles map[string]VehicleRecord
}

func NewFleetTracker() *FleetTracker {
	return &FleetTracker{vehicles: make(map[string]VehicleRecord)}
}

func (tracker *FleetTracker) Upsert(record VehicleRecord) VehicleRecord {
	tracker.mu.Lock()
	defer tracker.mu.Unlock()

	if record.UpdatedAt.IsZero() {
		record.UpdatedAt = time.Now().UTC()
	}

	tracker.vehicles[record.VehicleID] = record
	return record
}

func (tracker *FleetTracker) Snapshot() []VehicleRecord {
	tracker.mu.RLock()
	defer tracker.mu.RUnlock()

	snapshot := make([]VehicleRecord, 0, len(tracker.vehicles))
	for _, record := range tracker.vehicles {
		snapshot = append(snapshot, record)
	}

	sort.Slice(snapshot, func(left int, right int) bool {
		return snapshot[left].VehicleID < snapshot[right].VehicleID
	})

	return snapshot
}

func (tracker *FleetTracker) HealthyFraction() float64 {
	tracker.mu.RLock()
	defer tracker.mu.RUnlock()

	if len(tracker.vehicles) == 0 {
		return 0
	}

	healthy := 0
	for _, record := range tracker.vehicles {
		if record.Healthy {
			healthy++
		}
	}

	return float64(healthy) / float64(len(tracker.vehicles))
}
